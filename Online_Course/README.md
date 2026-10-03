# CS 5001 Online Course Demos

Runnable demonstrations for the 15-minute online modules. The demos are intentionally small, inspectable, and suitable for live recording.

## Modules

1. **AI-Augmented Software Engineering Crash Course** — end-to-end failing-test preview
2. **How LLMs Work** — transparent next-token/context simulation
3. **LLMs in Software Engineering** — debugging, repair, tests, documentation
4. **Prompt Engineering for Software Engineers** — weak vs structured prompts
5. **Prompt Patterns and Problem Decomposition** — Persona, Flipped Interaction, Question Refinement, Cognitive Verifier, Reflection
6. **RAG: Giving AI Project Knowledge** — retrieval and grounded prompt construction
7. **Building a RAG Pipeline** — chunking, local vectors, cosine similarity, top-k retrieval
8. **Building Your First CLI AI Agent** — Observe, Decide, Act, Evaluate loop
9. **Tool Use and Reflection** — explicit tool registry, verification, critique, retry
10. **Planning and Multi-Agent Systems** — planner, coder, tester, reviewer
11. **Building a Personalized AI Assistant** — allowlisted controller, workspace boundary, audit log
12. **AI Agent Orchestration** — routing, verification, retry, finish/escalation
13. **MCP: Connecting Agents to Tools** — dependency-free teaching model of schemas and structured tool calls
14. **A2A and Agentic Protocols** — dependency-free teaching model of structured agent-to-agent messages
15. **Engineering a Controlled AI-Augmented System** — validation, least capability, boundaries, limits, audit

## Important teaching convention

Some demos deliberately model an LLM, MCP, or A2A behavior locally so the recording is deterministic and requires no API key. Those modules label the simulation explicitly. They should not be presented as conforming implementations of external protocols or as measurements from production models.

## Running

Each module has its own README. Most executable demos use only the Python standard library; tests use pytest.

Example:

```bash
cd Online_Course/Module_12_Orchestration
python orchestration.py
pytest -q
```

The modules progressively evolve the same software-engineering story from prompting and context through RAG, agents, orchestration, protocols, and controlled execution.
