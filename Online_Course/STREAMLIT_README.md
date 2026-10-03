# CS 5001 Streamlit Demo Suite

Every online-course module is now an independently runnable Streamlit application.

## Run any module

Install dependencies once:

```bash
pip install -r Online_Course/requirements.txt
```

Then run the module you are recording. For example:

```bash
streamlit run Online_Course/Module_01_Crash_Course_Demo/streamlit_app.py
streamlit run Online_Course/Module_02_LLM_Basics/streamlit_app.py
streamlit run Online_Course/Module_03_LLM_for_SE/streamlit_app.py
```

The same pattern continues through Module 15.

## Architecture

Each `Module_XX_...` directory contains its own `streamlit_app.py`. This makes every 15-minute module self-contained for lecture recording and student demonstration.

The course-level `Online_Course/streamlit_app.py` remains as an optional all-modules navigator. The per-module applications are the primary recording interfaces.

Original Python logic and tests remain in each module so students can inspect and test the underlying implementation.

## Accuracy convention

Some modules intentionally use deterministic teaching simulations so demonstrations are reproducible and require no API key. Those pages identify this explicitly. The MCP and A2A modules demonstrate the concepts and structured interactions but do not claim conformance with a current external protocol SDK.
