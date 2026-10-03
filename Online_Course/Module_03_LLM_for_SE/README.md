# Module 3: LLMs in Software Engineering

Use one small function to demonstrate debugging, program repair, test generation, and documentation.

## Run
```bash
cd Online_Course/Module_03_LLM_for_SE
pytest -q
```

## Demo prompts
1. **Debug:** `Inspect se_tasks.py and test_se_tasks.py. Explain why the tests fail. Do not edit anything.`
2. **Repair:** `Make the minimum implementation change required by the documented requirements. Do not modify tests.`
3. **Tests:** `Suggest additional edge-case tests and state what requirement each verifies.`
4. **Docs:** `Suggest a concise documentation improvement without changing behavior.`

Run the tests after AI-generated changes. The teaching point is verification.
