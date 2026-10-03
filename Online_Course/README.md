# CS 5001 Online Course Demos

The 15 online-course demonstrations now share one **Streamlit presentation layer** for consistent lecture recording, while the original module Python files remain available as inspectable implementation and testing exercises.

## Run the complete demo suite

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r Online_Course/requirements.txt
streamlit run Online_Course/streamlit_app.py
```

Then use the Streamlit sidebar to move sequentially through Modules 1–15.

## Modules

1. **AI-Augmented Software Engineering Crash Course** — failing test → prompt → context → tools → agent → protocols
2. **How LLMs Work** — transparent next-token/context simulation
3. **LLMs in Software Engineering** — debugging and repair with verification
4. **Prompt Engineering for Software Engineers** — weak vs structured prompts
5. **Prompt Patterns and Problem Decomposition** — Persona, Flipped Interaction, Question Refinement, Cognitive Verifier, Reflection
6. **RAG: Giving AI Project Knowledge** — retrieval and grounded response behavior
7. **Building a RAG Pipeline** — chunking, overlap, and top-k retrieval
8. **From LLM to AI Agent** — Observe, Decide, Act, Evaluate
9. **Tool Use and Reflection** — verification, critique, retry
10. **Planning and Multi-Agent Systems** — planner, coder, tester, reviewer
11. **Building a Personalized AI Assistant** — allowlisted controller and audit boundary
12. **AI Agent Orchestration** — routing, verification, bounded retry
13. **MCP: Connecting Agents to Tools** — tool schemas and structured calls
14. **A2A and Agentic Protocols** — structured agent-to-agent messages
15. **Security, Responsible Use, and the Complete System** — allowlists, limits, audit, verification, human oversight

## Teaching convention

The Streamlit app is a presentation and interaction layer. Some demos deliberately model LLM, RAG, agent, MCP, or A2A behavior locally so recordings are deterministic and require no API key. The UI labels these cases explicitly.

The MCP and A2A demonstrations are conceptual teaching simulations. They must not be presented as conforming implementations of a current external protocol SDK.

The original module scripts and tests remain in their directories. They are useful for source inspection, exercises, and unit testing, while `streamlit_app.py` is the recommended interface for lecture/demo recording.

See `STREAMLIT_README.md` for the recording workflow.
