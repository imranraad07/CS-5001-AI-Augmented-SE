# Module 11: Building a Personalized AI Assistant

The demo focuses on the **controller layer**, not on a specific local LLM. Only predefined capabilities are available, arguments are constrained to a workspace, and actions are logged.

Run:
```bash
cd Online_Course/Module_11_Personal_Assistant
python personal_assistant.py
pytest -q
```

During recording, show a permitted read/write action, then demonstrate rejection of an unknown command and a path that escapes the workspace. Contrast this with giving an LLM arbitrary shell access.
