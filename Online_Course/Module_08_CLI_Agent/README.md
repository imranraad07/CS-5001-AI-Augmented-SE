# Module 8: Building Your First CLI AI Agent

A deterministic teaching agent demonstrates the control loop without requiring an API key. The `decide` method stands in for the LLM decision step and is explicitly a simulation.

Run:
```bash
cd Online_Course/Module_08_CLI_Agent
python cli_agent.py
pytest -q
```

Trace Observe → Decide → Act → Evaluate → Stop. Then explain where a real LLM, prompt controller, repository tools, sandbox, and verification layer would plug in.
