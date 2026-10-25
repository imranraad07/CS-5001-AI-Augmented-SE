# Module 1: Speaking Script and Screen Actions

**Target:** 18 minutes, including model waiting time, screen actions, manual
tracing, and learner pauses. This is a demonstration script, not 18 minutes
of continuous narration. Rehearse and adjust pauses for the recording machine.

## 0:00-2:00 | Define the task

[Open the app after checking Ollama. Reset the demonstration. Show stage 1.]

Welcome to AI-Augmented Software Engineering. We will start with a small
engineering problem and use it to introduce the workflow we will study in
this course. A checkout function is calculating a discount incorrectly.
Our task is to investigate the defect, make a focused change, and examine
whether the available evidence supports accepting that change.

The function accepts a subtotal and a discount percentage. It should reject
invalid inputs and return the discounted amount rounded to two decimal places.
For a subtotal of 80 and a discount of 25 percent, what should it return?

[Pause for an answer. Point to the implementation and trace its arithmetic.]

Twenty-five percent of 80 is 20, so the expected total is 60. This code
subtracts 25 directly and produces 55. We have a specific behavioral mismatch.
We also have constraints: preserve the function interface, input validation,
and rounding. Those constraints are part of the task.

## 2:00-4:00 | Establish the baseline

[Click Run baseline pytest. Read the actual output.]

Before changing anything, we run the tests. The prepared example is designed
to produce four passes and one failure. Read what happened in this run.
Which assertion failed, and what does it tell us?

[Inspect the expected and observed values. Trace the relevant test.]

A failure gives us concrete feedback. The passing tests also matter because
we want to retain the behavior they exercise. We will return to the same suite
after the implementation changes. That lets us compare observed behavior
before and after the change.

## 4:00-7:00 | Compare prompts

[Show stage 2. Select Vague; display the exact submitted request. Generate
if the recording budget permits. Select Structured and generate a proposal.]

Our first instruction is simply: fix this code. The application includes
the implementation with that request. Examine the actual response. A vague
instruction may still produce a useful answer for a small, obvious defect.
We should evaluate what happens rather than assume that it must fail.

Now compare the structured instruction. It identifies the percentage-discount
behavior and asks the model to preserve the signature, validation, and rounding.
It also requests the minimum change and excludes new dependencies.

[Read the response and compare it with the stated constraints.]

The purpose of these instructions is to communicate what counts as an
acceptable change. We can inspect whether the response addresses those
conditions. At this stage, the response is only a text proposal. This button
has not edited the project or executed the proposed code.

## 7:00-9:00 | Introduce context

[Show the protected tests. Select Include test context. Generate again only
if time permits; otherwise inspect the request construction on screen.]

The instruction is one part of the request. The project information supplied
with it is another. These tests show concrete expectations: valid totals,
invalid inputs, and the percentage calculation that currently fails.

What information would you want if the defect involved several files?

[Pause for a response. Point to the exact submitted request.]

For this small example, we can supply the relevant files directly. Larger
projects motivate methods for locating useful context. Later modules cover
retrieval-augmented generation. Here we are introducing that motivation;
we have not built a RAG pipeline.

## 9:00-13:00 | Observe the agent

[Show stage 3. Read the goal and click Run agent. Explain events as they appear.]

Now we give the system a goal and access to repository tools. It can request
a file, search text, change the implementation, and run tests. A program
executes those tool requests and supplies the results back to the model.
The model can then choose its next action.

Watch the actual events. Which file does it inspect? Does it run tests before
editing? What content does it write? Does it test the change afterward?

[Discuss only actions shown in the log. Allow time to inspect tool arguments
and results. Do not narrate an action before it occurs.]

In this module, the write tool accepts only the checkout implementation file.
A request to overwrite a test is rejected by that tool. This is stronger than
merely asking the model to leave tests alone. The disposable workspace lets
us reset the example for another run.

The agent has a finite step limit. If it stops without completing the task,
we will inspect that outcome. A completion message by itself is not evidence
that the implementation meets our requirements.

[If inference or tool execution fails, explain the visible error. If the
segment exceeds four minutes, pause the recording and label any time cut.
Do not substitute a successful outcome for the observed run.]

## 13:00-16:00 | Review and verify

[Show stage 4, the actual code diff, and independent pytest results.]

Let us examine what changed. A suitable correction multiplies the subtotal
by one minus the discount percentage divided by 100. Compare the actual diff
with that behavior. Check whether validation, rounding, and the public
interface remain intact. Look for unrelated edits as well.

[Trace 80 and 25 through the actual candidate. Inspect the test-integrity
message. Read the actual verification output.]

The application runs pytest independently after the agent returns, including
when the agent stops with an error or reaches its step limit. A passing result
means this candidate passed the current suite. A failing result means we need
to inspect the reported failure before accepting the change.

What is missing from these tests? We might examine a 100-percent discount,
a fractional percentage, or a rounding boundary. Passing the existing tests
does not establish correct behavior for every possible input.

[Pause for learners to propose one additional test and explain its purpose.]

## 16:00-18:00 | Connect the workflow to the course

[Keep the diff and results visible; recap the four stages.]

We began with a behavioral requirement and a reproducible failure. We compared
instructions, examined relevant context, observed tool use, and reviewed the
result using code inspection and executable tests.

The interface brings those steps together, but the engineering questions
remain central. What does the system know? What can it change? What evidence
supports the result? When should a developer accept or reject the change?

Later modules explain LLM basics and prompting, then retrieval, tools, and
agent design. We will also examine planning, coordination, and protocols.
This demonstration introduces the questions those topics help us investigate.

Before we finish, answer this: if a generated change passes every test you
supplied, what would you examine before accepting it into a larger project?

[Pause. Discuss compatibility with callers, missing cases, side effects,
and whether the change stayed within scope. Close at the target duration.]
