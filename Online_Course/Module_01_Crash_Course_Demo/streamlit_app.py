"""An observable, resettable opening demonstration using real local inference."""
from pathlib import Path
import difflib
import sys

MODULE = Path(__file__).resolve().parent
COURSE = MODULE.parent
for directory in (COURSE, MODULE):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import streamlit as st
from shared.agent import run_agent
from shared.demo_project import create_workspace
from shared.ollama_client import OllamaClient
from demo_tools import DemoTools

st.set_page_config(page_title='Module 1 | AI-Augmented SE', layout='wide')
st.title('Module 1: AI-Augmented Software Engineering')
st.caption('18-minute crash course: requirement, prompt, tools, review, verification')

with st.sidebar:
    st.header('Local model')
    base_url = st.text_input('Ollama URL', 'http://localhost:11434')
    model = st.text_input('Chat model', 'qwen3:4b')
    if st.button('Check connection'):
        models = OllamaClient(base_url, model).models()
        if models:
            st.success('Ollama connected')
            st.write(models)
        else:
            st.error('Ollama is unavailable or has no installed models.')
    st.caption('Start Ollama and download the chat model before recording.')
    if st.button('Reset demonstration'):
        for key in list(st.session_state):
            if key.startswith('m1_'):
                del st.session_state[key]
        st.rerun()

if 'm1_workspace' not in st.session_state:
    st.session_state.m1_workspace = str(create_workspace())
    initial = DemoTools(st.session_state.m1_workspace)
    st.session_state.m1_original = initial.read_file('src/checkout.py')
    st.session_state.m1_tests = initial.read_file('tests/test_checkout.py')
    st.session_state.m1_events = []

tools = DemoTools(st.session_state.m1_workspace)
client = OllamaClient(base_url, model)


def show_event(event):
    if event['type'] == 'tool':
        with st.expander('Tool: ' + event['name'], expanded=True):
            st.json(event['arguments'])
            result = event['result']
            if isinstance(result, dict) and 'output' in result:
                st.code(result['output'], wrap_lines=True)
            elif isinstance(result, dict):
                st.json(result)
            else:
                st.code(str(result), wrap_lines=True)
    elif event.get('content'):
        st.markdown(event['content'])


def show_tests(result):
    st.code(result['output'], wrap_lines=True)
    if result['returncode'] == 0:
        st.success('Current test suite passed. This is limited test evidence.')
    else:
        st.error('Verification failed. Inspect the test output.')


st.header('1. Understand and reproduce')
st.write('Apply a percentage discount, preserve the public interface, reject '
         'invalid inputs, and round to two decimal places. '
         'For subtotal 80 and discount 25%, the expected total is 60, not 55.')
left, right = st.columns(2)
with left:
    st.subheader('Starting implementation')
    st.code(st.session_state.m1_original, language='python', wrap_lines=True)
with right:
    st.subheader('Protected tests')
    st.code(st.session_state.m1_tests, language='python', wrap_lines=True)

if st.button('Run baseline pytest'):
    if tools.read_file('src/checkout.py') != st.session_state.m1_original:
        st.warning('Reset the demonstration to reproduce the original baseline.')
    else:
        try:
            st.session_state.m1_baseline = tools.run_tests()
        except Exception as exc:
            st.error(f'Baseline execution failed: {exc}')
if 'm1_baseline' in st.session_state:
    show_tests(st.session_state.m1_baseline)

st.header('2. Compare prompts')
st.caption('Text-only requests do not edit the repository or execute tests. '
           'Compare the actual responses; a vague prompt may still succeed.')
style = st.radio('Prompt style', ['Vague', 'Structured'])
default_prompt = ('Fix this code.' if style == 'Vague' else
    'Correct the percentage-discount calculation. Preserve the function '
    'signature, input validation, and rounding. Make the minimum change; '
    'do not add dependencies. Explain the proposed change.')
with st.form('prompt_form'):
    prompt = st.text_area('Instruction', default_prompt, key='prompt_' + style)
    include_tests = st.checkbox('Include test context', value=False)
    generate = st.form_submit_button('Generate text-only proposal')
if generate:
    request = prompt + '\n\nImplementation:\n' + st.session_state.m1_original
    if include_tests:
        request += '\n\nTests:\n' + st.session_state.m1_tests
    st.session_state.m1_request = request
    st.session_state.pop('m1_proposal', None)
    try:
        with st.spinner('Waiting for the local model...'):
            st.session_state.m1_proposal = client.generate(request)
    except Exception as exc:
        st.error(f'Model request failed: {exc}')
if 'm1_request' in st.session_state:
    with st.expander('Last submitted request'):
        st.code(st.session_state.m1_request, wrap_lines=True)
if 'm1_proposal' in st.session_state:
    st.markdown(st.session_state.m1_proposal)

st.header('3. Observe the agent')
goal = st.text_area('Agent goal',
    'Investigate and fix the failing percentage-discount behavior. '
    'Preserve the function signature, validation, and rounding. '
    'Do not modify tests or add dependencies. Make the minimum '
    'implementation change and run tests after editing.')
st.caption('The agent may read/search files and run pytest. '
           'Its write tool permits only src/checkout.py.')
run = st.button('Run agent')
activity = st.container()
if run:
    st.session_state.m1_events = []
    for key in ('m1_final', 'm1_status', 'm1_error'):
        st.session_state.pop(key, None)

    def on_event(event):
        st.session_state.m1_events.append(event)
        with activity:
            show_event(event)

    try:
        with st.spinner('Agent running; tool events appear as actions finish...'):
            result = run_agent(client, tools, goal, on_event=on_event)
            st.session_state.m1_status = result['status']
    except Exception as exc:
        st.session_state.m1_error = str(exc)
else:
    with activity:
        for event in st.session_state.m1_events:
            show_event(event)
if 'm1_status' in st.session_state:
    st.info('Agent stop reason: ' + st.session_state.m1_status +
            '. This status alone does not establish correctness.')
if 'm1_error' in st.session_state:
    st.error('Agent stopped: ' + st.session_state.m1_error)

st.header('4. Review and verify')
current = tools.read_file('src/checkout.py')
st.code(current, language='python', wrap_lines=True)
diff = ''.join(difflib.unified_diff(
    st.session_state.m1_original.splitlines(keepends=True),
    current.splitlines(keepends=True), fromfile='before/checkout.py',
    tofile='after/checkout.py'))
if diff:
    st.code(diff, language='diff', wrap_lines=True)
else:
    st.info('No implementation changes yet.')
intact = tools.read_file('tests/test_checkout.py') == st.session_state.m1_tests
if not intact:
    st.error('Test integrity check failed. Reset the demonstration.')
if run or st.button('Run independent verification'):
    try:
        st.session_state.m1_final = tools.run_tests()
    except Exception as exc:
        st.error(f'Test execution failed: {exc}')
if 'm1_final' in st.session_state:
    show_tests(st.session_state.m1_final)
    if intact:
        st.caption('Test file matches the original snapshot.')
st.write('Review the diff, public interface, validation, and test coverage '
         'before accepting the change. Passing tests cover only tested cases.')
