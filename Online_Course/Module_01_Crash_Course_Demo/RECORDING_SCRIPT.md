# Recording Script: Module 1 Demo

Target: approximately 10 to 15 minutes.

## Opening

"Rather than starting with definitions, let us start with a software engineering problem. This repository has a failing test. Our goal is to fix it without changing the tests or breaking the existing interface."

Run:

```bash
pytest -q
```

Point out that four tests pass and one fails.

## Stage 1: LLM

Show `src/checkout.py` without the test and ask:

```text
Fix this code.
```

Narration:

"This is the simplest form of AI-assisted software engineering. I give an LLM some code and ask for an answer. The problem is that the model does not yet know what the rest of this project expects."

## Stage 2: Prompt Engineering

Use the engineered prompt from README.md.

Narration:

"Now the task, constraints, and expected behavior of the interaction are clearer. This is our first step toward prompt engineering. But the model still needs project information."

## Stage 3: Context and RAG

Reveal `tests/test_checkout.py`.

Narration:

"For this tiny repository I can provide the relevant files manually. In a large repository we need a systematic way to find relevant information. That motivates retrieval-augmented generation, or RAG: retrieve useful context, add it to the model's context, then generate."

## Stage 4: Tools

Move to an agent-capable coding interface and ask it to investigate without editing.

Narration:

"Instead of manually copying files and terminal output, we can give the AI controlled tools. It can inspect files, search the repository, and run tests. The model is no longer limited to producing text."

## Stage 5: Agent

Give the agent the fix task and constraints.

Narration while it works:

"Notice the change in interaction. I am giving the system a goal rather than asking for a single answer. It observes the environment, decides what to inspect, acts, and verifies the result."

When tests pass:

"Verification matters. The important evidence is not that the model says the bug is fixed. The test suite now says five tests pass."

## Stage 6: Preview the Rest of the Course

Show:

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

Narration:

"This small example is the roadmap for the course. We started with an LLM response, improved the instruction, supplied context, added tools, and moved toward an agent that can act and verify. Later we will add reflection and planning, coordinate multiple agents, and examine protocols such as MCP and A2A."

## Closing

Show the passing test output.

"The interesting part is not simply that AI can generate code. The software engineering questions are how we provide context, what actions the system can perform, how we verify those actions, how we recover from failure, and how we coordinate increasingly capable components. Those are the questions we will study in AI-Augmented Software Engineering."
