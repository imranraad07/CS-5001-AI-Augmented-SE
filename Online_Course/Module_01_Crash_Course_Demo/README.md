# Module 1: AI-Augmented Software Engineering Crash Course

Target: 18 minutes including live generation, inspection, and learner pauses.
Use `LECTURE_NOTES.md` for the teaching outline and `RECORDING_SCRIPT.md`
for spoken narration and screen actions.

## Learning outcomes

Learners will identify a behavioral defect, supply task constraints and context,
observe repository tool use, and evaluate a generated change using a diff and
actual test results. Later modules explain the underlying concepts in depth.

## Scenario

`calculate_total(80, 25)` should return `60.00`. The starting implementation
subtracts 25 dollars and returns `55.00`. The initial suite has four passing
tests and one failing percentage-discount test. These are expected results;
always show the actual execution output during the lesson.

## Setup before recording

From this module directory, use Python 3.10 or later:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
ollama pull qwen3:4b
python -m streamlit run streamlit_app.py
```

On Windows, activate with `.venv\Scripts\activate`. Start Ollama separately
if its local service is not already running. The app defaults to
`http://localhost:11434`; change the sidebar settings if needed. Rehearse
with the selected tool-capable model and hardware. Generation time and
agent success vary; no successful model outcome is assumed.

## Recording sequence

| Minutes | Screen action | Teaching purpose |
| --- | --- | --- |
| 0-2 | Show requirements, implementation, tests | Define the defect |
| 2-4 | Run baseline pytest | Establish observable evidence |
| 4-7 | Compare vague and structured requests | Introduce instructions and constraints |
| 7-9 | Include test context | Explain relevant project context |
| 9-13 | Run the agent and inspect live events | Demonstrate tools and an agent loop |
| 13-16 | Review diff and independent verification | Evaluate changes and test integrity |
| 16-18 | Recap and exit question | Connect to later modules |

For a 15-minute version, generate only the structured response and read the
vague prompt without running it. For a 20-minute version, allow two extra
minutes for inspecting a failure or discussing missing tests. Limit the live
agent segment to four minutes in the lesson; edit out extended waiting in a
recording, clearly marking any time cut. Do not present stored output as live.

## Interface behavior

The app creates a disposable workspace; agent edits do not modify this module's
tracked `src/checkout.py`. Reset creates a fresh workspace and clears results.
Baseline output, model proposal, events, and final results persist across
ordinary interface interactions. Events appear as completed actions arrive,
not as token-level streaming. Text-only proposals never apply changes.

The Module 1 write tool accepts only `src/checkout.py`. The app also compares
the test file to its original snapshot. This tool restriction is not an OS
sandbox: running generated Python executes code on the host. Use the local
teaching environment with the disposable example, not an exposed public app.

Successful pytest execution is labeled as test evidence, not proof of complete
correctness. Review the diff for unchanged signature, validation, and rounding.
Repository text search previews retrieval; this demo does not implement a RAG
pipeline, multi-agent coordination, MCP, or A2A.
