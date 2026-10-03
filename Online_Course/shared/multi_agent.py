"""Role-based multi-agent workflow backed by Ollama."""
from __future__ import annotations

def ask(client,role,task,context=""):
    return client.generate(f"Task: {task}\n\nContext:\n{context}",system=f"You are the {role} in a software-engineering team. Be concrete, concise, and evidence-driven.")

def run_team(client,goal,code,test_output=""):
    plan=ask(client,"planner",goal,code)
    implementation=ask(client,"coder",goal,f"PLAN:\n{plan}\n\nCODE:\n{code}")
    tests=ask(client,"tester","Design verification for the proposed change",f"GOAL:\n{goal}\n\nPROPOSAL:\n{implementation}\n\nCURRENT TEST OUTPUT:\n{test_output}")
    review=ask(client,"reviewer","Review the proposal and verification evidence",f"GOAL:\n{goal}\n\nPLAN:\n{plan}\n\nPROPOSAL:\n{implementation}\n\nTESTER:\n{tests}")
    return {"planner":plan,"coder":implementation,"tester":tests,"reviewer":review}
