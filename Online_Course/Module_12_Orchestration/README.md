# Module 12: AI Agent Orchestration

This workflow makes coordination visible: planner → coder → tester → retry → reviewer → finish.

Run:
```bash
cd Online_Course/Module_12_Orchestration
python orchestration.py
pytest -q
```

The first attempt deliberately fails so the orchestrator must route the workflow through retry. Use the event log to answer: who does what, in what order, with what result, and when do we retry or stop?
