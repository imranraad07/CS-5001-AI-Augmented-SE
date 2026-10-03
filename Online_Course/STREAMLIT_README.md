# CS 5001 Streamlit Demo Suite

All 15 online-course demos are available through one Streamlit application.

## Run

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r Online_Course/requirements.txt
streamlit run Online_Course/streamlit_app.py
```

Use the sidebar to move sequentially through Modules 1–15.

## Teaching design

Each page is intentionally small enough for a live lecture recording. The UI exposes input, system behavior, evidence/output, and takeaway rather than hiding the mechanics.

Modules 2, 6, 7, 8, 13, and 14 explicitly label deterministic or simplified teaching simulations. In particular, MCP and A2A demonstrate course concepts but do not claim conformance with a current external protocol SDK.

The original Python implementations and tests remain in their module directories as inspectable source material and unit-test exercises. Streamlit is now the presentation/demo layer.

## Recording workflow

1. Start the Streamlit app once.
2. Select the module from the sidebar.
3. Reset widgets to defaults before recording.
4. Narrate the concept while changing only the controls relevant to that module.
5. End on visible verification/takeaway state.
6. Move to the next module.
