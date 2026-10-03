# Module 15: Engineering a Controlled AI-Augmented System

This final demo consolidates controls already introduced in the course: explicit capabilities, argument validation, workspace boundaries, action/iteration limits, logging, verification, and human oversight.

Run:
```bash
cd Online_Course/Module_15_Secure_AI_System
python secure_system.py
pytest -q
```

Record a successful allowlisted read, a denied tool request, and an action-limit failure. Finish by mapping these controls back onto the full architecture: user → orchestrator → agents → RAG/tools → verification → human.
