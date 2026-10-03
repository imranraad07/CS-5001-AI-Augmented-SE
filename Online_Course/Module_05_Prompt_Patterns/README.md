# Module 5: Prompt Patterns and Problem Decomposition

Runnable prompt builders for Persona, Flipped Interaction, Question Refinement, Cognitive Verifier, and Reflection.

## Run
```bash
cd Online_Course/Module_05_Prompt_Patterns
python prompt_patterns_demo.py
pytest -q
```

## Demo
Begin with the vague question `Why is this service returning 502 errors?`. Generate the patterns, send selected prompts to an LLM, and show how the interaction changes. The incident is intentionally under-specified, so do not claim a root cause without evidence.
