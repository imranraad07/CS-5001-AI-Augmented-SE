from __future__ import annotations
import streamlit as st

st.set_page_config(page_title="CS 5001 | AI-Augmented Software Engineering", page_icon="🤖", layout="wide")
MODULES=["01 · Crash Course","02 · How LLMs Work","03 · LLMs for Software Engineering","04 · Prompt Engineering","05 · Prompt Patterns & Decomposition","06 · RAG Basics","07 · RAG Pipeline","08 · From LLM to AI Agent","09 · Tool Use & Reflection","10 · Planning & Multi-Agent Systems","11 · Personalized AI Assistant","12 · Agent Orchestration","13 · MCP","14 · A2A & Agentic Protocols","15 · Secure Integrated System"]

def header(title,objective):
    st.title(title); st.caption("CS 5001 · AI-Augmented Software Engineering"); st.info(objective)
def checkout(subtotal,discount,fixed=False):
    return round(subtotal*(1-discount/100) if fixed else subtotal-discount,2)
def tokens(s):
    return [x.strip(".,:;!?()[]").lower() for x in s.split() if x.strip(".,:;!?()[]")]
def score(q,d):
    return len(set(tokens(q)) & set(tokens(d)))

module=st.sidebar.radio("Module",MODULES)
st.sidebar.markdown("---")
st.sidebar.caption("Interactive teaching demos. Deterministic simulations are labeled explicitly.")

if module.startswith("01"):
    header("Module 1 · AI-Augmented SE Crash Course","See the course progression from a weak LLM prompt to context, tools, an agent loop, orchestration, and protocols.")
    subtotal=st.number_input("Subtotal",0.0,10000.0,80.0,step=5.0); discount=st.slider("Discount (%)",0,100,25); fixed=st.toggle("Apply agent's proposed fix")
    actual=checkout(subtotal,discount,fixed); expected=round(subtotal*(1-discount/100),2)
    c1,c2,c3=st.columns(3); c1.metric("Expected",f"USD {expected:.2f}"); c2.metric("Implementation",f"USD {actual:.2f}"); c3.metric("Test","PASS" if actual==expected else "FAIL")
    st.code("total = subtotal * (1 - discount_percent / 100)" if fixed else "total = subtotal - discount_percent",language="python")
    st.markdown("**Progression:** Prompt → Context/RAG → Tools → Agent → Reflection/Planning → Multi-Agent → Orchestration → MCP/A2A")
elif module.startswith("02"):
    header("Module 2 · How LLMs Work","Build intuition for next-token prediction and the effect of context.")
    st.warning("Teaching simulation: these probabilities are illustrative, not measurements from a real LLM.")
    context=st.selectbox("Context",["Mary had a little","for i in range(","items = ['a', 'b', 'c']\nfor i in range("])
    options={"Mary had a little":{"lamb":.78,"girl":.08,"house":.06,"dog":.04,"car":.04},"for i in range(":{"10":.40,"len(items)":.25,"n":.20,"100":.10,"x":.05},"items = ['a', 'b', 'c']\nfor i in range(":{"len(items)":.65,"3":.20,"10":.08,"n":.05,"x":.02}}[context]
    st.bar_chart(options); st.code(context+max(options,key=options.get))
    st.markdown("The model generates one token at a time conditioned on the context available to it.")
elif module.startswith("03"):
    header("Module 3 · LLMs for Software Engineering","Explore code generation, debugging, testing, review, and documentation while keeping verification in the loop.")
    raw=st.text_input("Username input","  Alice.Smith  "); buggy=raw.strip(); repaired=raw.strip().lower()
    st.code('def normalize_username(value):\n    return value.strip()  # missing case normalization',language="python"); st.write("Current output:",buggy)
    if st.button("Apply suggested repair"): st.success(f"Repaired output: {repaired}"); st.code('return value.strip().lower()',language="python")
    st.caption("Generated code is a proposal. Tests and review provide evidence.")
elif module.startswith("04"):
    header("Module 4 · Prompt Engineering","Compare vague instructions with a structured software-engineering prompt.")
    task=st.text_input("Task","Fix the checkout bug"); weak="Fix this code."
    strong=f"""CONTEXT: A Python checkout project has a failing percentage-discount test.
TASK: {task}
CONSTRAINTS: Preserve public interfaces; do not modify tests; add no dependencies; make the minimum change.
EXPECTED OUTPUT: Explain the failure, propose the smallest patch, then verify it.
VERIFICATION: Run the relevant tests after the change."""
    left,right=st.columns(2); left.subheader("Weak prompt"); left.code(weak); right.subheader("Engineered prompt"); right.code(strong)
elif module.startswith("05"):
    header("Module 5 · Prompt Patterns & Decomposition","Use prompt patterns to turn an underspecified incident into an evidence-driven investigation.")
    incident=st.text_area("Incident","Users intermittently receive Nginx 502 responses."); pattern=st.selectbox("Pattern",["Persona","Flipped Interaction","Question Refinement","Cognitive Verifier","Reflection"])
    prompts={"Persona":"Act as an SRE. Diagnose using observable evidence before proposing changes.","Flipped Interaction":"Ask me one diagnostic question at a time until you have enough evidence to form a hypothesis.","Question Refinement":"Rewrite my incident report into a precise debugging question, then explain what information is missing.","Cognitive Verifier":"Break the diagnosis into checks: reproduce, classify failure, form hypothesis, validate, then fix.","Reflection":"Review the proposed diagnosis. Identify unsupported assumptions and request evidence for them."}
    st.code(f"{prompts[pattern]}\n\nIncident: {incident}"); st.markdown("**Decomposition:** observe → classify → hypothesize → validate → fix → verify")
elif module.startswith("06"):
    header("Module 6 · RAG: Giving AI Project Knowledge","Retrieve relevant project evidence before generation.")
    st.warning("Teaching implementation: keyword retrieval + templated grounded response, not an external LLM.")
    docs={"CONTRIBUTING.md":"Before merge, run unit tests and lint checks. Do not bypass failing tests.","RUNBOOK.md":"For checkout incidents, inspect service logs and reproduce the failure before deployment.","OWNERS.md":"Checkout changes require review from the payments maintainers."}
    q=st.text_input("Ask the project","What checks are required before merge?"); ranked=sorted(docs.items(),key=lambda x:score(q,x[1]),reverse=True); k=st.slider("Top-k",1,3,2)
    for name,text in ranked[:k]: st.write(f"**{name}** · score {score(q,text)}"); st.code(text)
    if st.button("Generate grounded answer"):
        if score(q,ranked[0][1])==0: st.info("I don't know from the supplied sources.")
        else: st.success(f"Use the retrieved evidence above and cite {', '.join(n for n,_ in ranked[:k])}.")
elif module.startswith("07"):
    header("Module 7 · Building a RAG Pipeline","Inspect chunking, overlap, retrieval, and how configuration changes results.")
    st.warning("Teaching implementation: lexical vectors make the pipeline inspectable; they are not production embeddings.")
    text=st.text_area("Document","Before merge run unit tests and lint checks. Checkout incidents should be reproduced before deployment. Changes require review."); size=st.slider("Chunk size (words)",3,12,7); overlap=st.slider("Overlap",0,size-1,2)
    words=text.split(); chunks=[]; i=0
    while i<len(words):
        chunks.append(" ".join(words[i:i+size]))
        if i+size>=len(words): break
        i+=size-overlap
    st.write("Chunks")
    for j,c in enumerate(chunks): st.code(f"{j+1}: {c}")
    q=st.text_input("Retrieval query","What should happen before merge?",key="m7"); ranked=sorted(enumerate(chunks),key=lambda x:score(q,x[1]),reverse=True); st.success(f"Top chunk: {ranked[0][1] if ranked else 'None'}")
elif module.startswith("08"):
    header("Module 8 · From LLM to AI Agent","Follow an Observe → Decide → Act → Evaluate loop with a bounded iteration count.")
    st.warning("Deterministic agent simulation: the decision policy stands in for an LLM so the classroom demo is reproducible."); max_iter=st.slider("Maximum iterations",1,5,3)
    if st.button("Run agent"):
        rows=[("Observe","Percentage test fails: expected 60, got 55"),("Decide","Inspect percentage calculation"),("Act","Replace subtraction with percentage formula"),("Evaluate","5 tests pass"),("Stop","Goal verified")]
        for phase,msg in rows[:max_iter+2]: st.write(f"**{phase}:** {msg}")
        st.success("Goal verified.")
elif module.startswith("09"):
    header("Module 9 · Tool Use & Reflection","See how tool feedback can trigger critique and revision."); attempt=st.radio("Attempt",[1,2],horizontal=True)
    if attempt==1: st.code("total = subtotal - discount_percent",language="python"); st.error("run_tests → 1 failed, 4 passed"); st.write("Reflection: the implementation treats a percentage as currency. Revise.")
    else: st.code("total = subtotal * (1 - discount_percent / 100)",language="python"); st.success("run_tests → 5 passed"); st.write("Reflection: verification passed. Stop.")
    st.caption("Conceptual tools: read_file, edit_file, run_tests.")
elif module.startswith("10"):
    header("Module 10 · Planning & Multi-Agent Systems","Decompose a feature and route subtasks to specialized roles."); goal=st.text_input("Goal","Add coupon support to checkout")
    if st.button("Create plan"):
        for role,task in [("Planner","Clarify coupon requirements and affected interfaces"),("Coder","Implement minimal change"),("Tester","Add/execute behavioral tests"),("Reviewer","Check interface, edge cases, and evidence")]: st.write(f"**{role} →** {task}")
        st.success(f"Plan created for: {goal}")
elif module.startswith("11"):
    header("Module 11 · Personalized AI Assistant","Contrast controlled capabilities with arbitrary execution."); st.warning("The demo models a controller boundary. It does not execute arbitrary shell commands.")
    command=st.selectbox("Allowed command",["write_note","read_note"]); note=st.text_input("Note","Review checkout tests")
    if st.button("Execute controlled action"): st.success(f"{command} accepted by allowlist"); st.code(f"AUDIT: command={command!r}, argument={note!r}")
    st.error("Rejected design: LLM → arbitrary shell / arbitrary HTTP")
elif module.startswith("12"):
    header("Module 12 · AI Agent Orchestration","Coordinate planning, coding, testing, retry, and review.")
    if st.button("Run orchestrated workflow"):
        for e in ["Planner → define minimal bug-fix task","Coder attempt 1 → incorrect patch","Tester → FAIL","Orchestrator → retry","Coder attempt 2 → percentage formula","Tester → PASS","Reviewer → approve","Orchestrator → finish"]: st.write(e)
        st.success("Workflow complete after bounded retry.")
    st.markdown("Orchestration decides **who**, **what order**, **what context**, **constraints**, and **when to retry/stop**.")
elif module.startswith("13"):
    header("Module 13 · MCP: Connecting Agents to Tools","Understand MCP's role as a standardized interface for external capabilities."); st.warning("Teaching simulation only. This page demonstrates MCP concepts and tool schemas; it is not a conforming MCP server/client implementation.")
    tool=st.selectbox("Tool",["search_repo","run_tests"]); schemas={"search_repo":{"query":"string","path":"optional string"},"run_tests":{"path":"string"}}; st.json({"name":tool,"description":"Demo tool exposed to an agent","parameters":schemas[tool],"output":"structured result"})
    if st.button("Call tool"): st.json({"tool":tool,"result":{"passed":5,"failed":0}} if tool=="run_tests" else {"tool":tool,"result":["src/checkout.py","tests/test_checkout.py"]})
    st.markdown("Prompting guides reasoning · RAG retrieves knowledge · tool calling performs actions · MCP standardizes the tool interface.")
elif module.startswith("14"):
    header("Module 14 · A2A & Agentic Protocols","See structured agent-to-agent messages alongside tool access."); st.warning("Teaching simulation only. It does not claim conformance with a specific A2A SDK or protocol version.")
    sender=st.selectbox("Sender",["Planner","Coder","Tester","Reviewer"]); receiver=st.selectbox("Receiver",["Coder","Tester","Reviewer","Planner"]); task=st.text_input("Task","Fix the failing percentage-discount test")
    if st.button("Send structured message"): st.json({"from":sender,"to":receiver,"type":"task_request","task":task,"context":{"repo":"checkout-demo"},"expected_result":"structured status"})
    st.markdown("**Tool path:** Agent → MCP → Tool  \n**Collaboration path:** Agent → A2A → Agent")
elif module.startswith("15"):
    header("Module 15 · Security, Responsible Use & Complete System","Integrate grounding, controlled actions, verification, limits, audit, and human oversight.")
    requested=st.selectbox("Requested capability",["read_file","run_tests","arbitrary_shell","external_http"]); allowed={"read_file","run_tests"}; actions=st.slider("Actions already used",0,5,1); limit=3
    c1,c2=st.columns(2); c1.metric("Action budget",f"{actions}/{limit}"); c2.metric("Allowlisted","Yes" if requested in allowed else "No")
    if st.button("Authorize action"):
        if actions>=limit: st.error("DENIED: action budget exhausted. Escalate.")
        elif requested not in allowed: st.error("DENIED: capability is not allowlisted.")
        else: st.success("AUTHORIZED: validate arguments → execute in boundary → log → verify")
    st.code("User → Prompt/Plan → RAG → Agent/Orchestrator → Controlled Tools → Verification → Audit/Human Oversight")

st.divider(); st.caption("Course principle: AI output is not proof. Use project context, controlled capabilities, and software-engineering verification.")
