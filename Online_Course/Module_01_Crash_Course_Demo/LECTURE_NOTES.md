# Lecture Notes: Module 1

**Topic:** From a failing test to an inspected, tested AI-assisted change.
**Duration:** 18 minutes including demonstration and pauses.
**Prerequisites:** Basic Python functions, percentages, and unit-test familiarity.

## Core example

The checkout function should apply a percentage discount. For subtotal 80 and
25 percent discount, expected total is 60; the initial code produces 55.
The defect is `subtotal - discount_percent`. A suitable correction is
`subtotal * (1 - discount_percent / 100)`, preserving validation and rounding.
Keep the starting defect in the tracked source so learners can reproduce it.

## Concepts to explain

- Requirement: the behavior and constraints the implementation must satisfy.
- Prompt: the task instruction submitted to the model.
- Context: relevant code, tests, requirements, and observed failures.
- Tool: a callable action such as reading a file or running pytest.
- Agent loop: repeated model requests and tool results directed toward a goal.
- Verification: evidence from executing tests and inspecting the actual change.

## Teaching sequence

1. **0-2 minutes:** State the requirement; ask learners to predict the result.
2. **2-4 minutes:** Run the baseline; inspect the percentage assertion failure.
3. **4-7 minutes:** Compare vague and structured prompts. Do not claim that
   vague prompting necessarily fails; discuss the actual responses.
4. **7-9 minutes:** Reveal/include tests as context. Explain that larger
   projects motivate retrieval; distinguish this from implementing RAG.
5. **9-13 minutes:** Run the agent. Explain each actual read, search, write,
   and test action. Do not assume a particular action order or successful repair.
6. **13-16 minutes:** Inspect the diff, test-file integrity, and independent
   pytest output. If the run fails or reaches its step limit, explain the
   observed result. Reset and rehearse before a new attempt.
7. **16-18 minutes:** Recap requirements, context, actions, review, and evidence.
   Preview LLM basics, prompting, retrieval, tools, agents, and later protocols.

## Acceptance discussion

Check the function signature, validation, percentage arithmetic, rounding,
absence of unrelated changes, unchanged tests, and actual pytest results.
Five passing tests support only those tested cases. The suite does not cover
all behavior, such as 100-percent discounts, fractional discounts, or rounding
boundaries. Ask learners which test they would add and why.

## Instructor preparation

Download the model and install dependencies before class. Rehearse on the
recording machine. Use connection checking, then reset before the baseline.
Keep the code and logs readable at recording resolution. Allow about half the
lesson for actions, model latency, inspection, and learner responses rather
than continuous speech. Timing is a target and requires rehearsal.

## Exit questions

1. What additional context helped evaluate the proposed change?
2. What distinguishes a text-only proposal from the tool-using agent?
3. Why do passing tests alone not establish complete correctness?
