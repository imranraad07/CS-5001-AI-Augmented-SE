# Module 1: Checkout Agent Demo

A local Streamlit application using Ollama, repository tools, and real pytest execution.

## Setup

From this directory, use Python 3.10 or later:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
ollama pull qwen3:4b
python -m streamlit run streamlit_app.py
```

On Windows, activate with `.venv\Scripts\activate`. Start Ollama separately if its service is not running. The default URL is `http://localhost:11434`; configure the URL and chat model in the sidebar.

## Example behavior

The initial checkout implementation subtracts a percentage as a dollar amount. `calculate_total(80, 25)` returns 55 instead of 60. The prepared baseline suite is expected to report one failure and four passes.

The application supports text-only proposals and a tool-using agent. Text-only requests do not edit files. Agent events appear as completed actions arrive. Results persist across ordinary widget interactions. The review panel displays the implementation diff and independent pytest results.

## Workspace and tool permissions

Each session uses a disposable workspace. Reset creates a fresh workspace and clears displayed results. Tracked example source files are not changed by agent actions.

The Module 1 write tool accepts only `src/checkout.py`. The application also compares the test file with its initial snapshot. This restriction is not an OS sandbox: generated Python executes on the host. Use a local development environment rather than exposing the app publicly.

## Validation

```bash
python -m pytest -q test_demo_workflow.py
```

The regression tests check baseline failure, repaired-suite success, write restrictions, and callback reporting of rejected test edits. Model success depends on the selected model and runtime environment. Passing tests provide evidence for the tested cases only.
