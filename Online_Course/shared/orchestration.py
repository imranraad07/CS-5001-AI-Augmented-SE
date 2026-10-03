"""Bounded orchestration over the real Ollama tool-calling agent."""
from __future__ import annotations
from .agent import run_agent

def orchestrate(client,tools,goal,retries=2):
    attempts=[]
    for i in range(retries+1):
        result=run_agent(client,tools,goal,max_steps=8)
        verification=tools.run_tests()
        attempts.append({"attempt":i+1,"agent":result,"verification":verification})
        if verification["returncode"]==0:
            return {"status":"verified","attempts":attempts}
        goal += "\nPrevious attempt did not pass tests. Inspect the current repository and failure output, reflect, and try a different minimal fix."
    return {"status":"failed","attempts":attempts}
