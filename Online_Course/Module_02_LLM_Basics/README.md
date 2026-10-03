# Module 2: How LLMs Work

A transparent teaching simulation of next-token prediction and context. The probabilities are hand-written for instruction and are **not measurements from a production LLM**.

## Run
```bash
cd Online_Course/Module_02_LLM_Basics
python token_prediction_demo.py
pytest -q
```

## Demo
Run the natural-language example, then the generic code context, then add the `items` context. Show that changing context changes the continuation distribution. Close with: plausible continuation is not verified correctness.
