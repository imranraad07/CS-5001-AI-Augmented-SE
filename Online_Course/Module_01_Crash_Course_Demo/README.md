# Module 1: AI-Augmented Software Engineering Crash-Course Demo

This repository fragment is intentionally small and contains one deterministic bug. It is designed for a short screen-recorded opening demo.

## Scenario

A checkout function should apply a percentage discount. Four tests pass and one fails because the implementation subtracts the percentage as a dollar amount.

## Setup

From this directory:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
```

Expected starting result:

```text
....F
1 failed, 4 passed
```

The failing behavior is:

```python
calculate_total(80.00, 25)
```

Expected: `60.00`

Buggy result: `55.00`

## Recording sequence

### 1. Baseline

Run:

```bash
pytest -q
```

Establish the software-engineering goal: fix the failing test without modifying tests or public interfaces.

### 2. Simple LLM prompt

Show only `src/checkout.py` and ask:

```text
Fix this code.
```

Use this to discuss the weakness of vague prompts and missing repository context.

### 3. Engineered prompt

Use:

```text
A unit test is failing in this Python project.
Analyze the failure before proposing a change.

Constraints:
- Preserve the existing public interface.
- Do not modify the tests.
- Do not introduce new dependencies.
- Make the minimum necessary change.
- Ask for information you need before proposing a fix.
```

Use the model's request for more information to motivate context and retrieval.

### 4. Repository context

Reveal `tests/test_checkout.py` and the requirements in this README. Explain that a large repository cannot simply be pasted into every prompt. This motivates retrieval and RAG.

### 5. Tool use

In an agent-capable coding environment, give the model repository access and the tools needed to read files and run tests. Ask:

```text
Investigate the failing test. Do not modify anything yet.
```

The model should inspect the failure and relevant implementation.

### 6. Agent task

Ask:

```text
Fix the failing test.

Constraints:
- Do not modify tests.
- Preserve public interfaces.
- Do not add dependencies.
- Run the tests after making the change.
```

The intended correction is conceptually:

```python
total = subtotal * (1 - discount_percent / 100)
```

Run `pytest -q` again. Expected final result:

```text
.....
5 passed
```

### 7. Connect the demo to the course

Use the completed interaction to introduce the course progression:

```text
LLM
 -> Prompt Engineering
 -> Context / RAG
 -> Tool Use
 -> AI Agent
 -> Reflection and Planning
 -> Multi-Agent Systems
 -> Orchestration
 -> Agentic Protocols
```

Do not implement every later concept in this first demo. The working repository demonstrates the core transition from prompting to an agent using repository tools and verification. Planning, multi-agent orchestration, MCP, and A2A are previewed as the next abstractions.

## Reset after recording

Restore this line in `src/checkout.py`:

```python
total = subtotal - discount_percent
```

Then confirm that `pytest -q` returns one failure again.
