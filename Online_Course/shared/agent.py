"""Ollama tool-calling software-engineering agent."""
from __future__ import annotations
import json

SYSTEM="""You are a careful software-engineering agent working in a disposable repository.
Use tools to inspect evidence before editing. Never modify tests to hide a defect.
Make the smallest implementation change that satisfies the stated behavior.
Always run tests after a code change. Stop only after verification or when blocked."""

def run_agent(client,tools,goal,max_steps=8,on_event=None):
    messages=[{"role":"system","content":SYSTEM},{"role":"user","content":goal}]
    events=[]
    def emit(e):
        events.append(e)
        if on_event: on_event(e)
    for step in range(max_steps):
        msg=client.chat(messages,tools=tools.schemas())
        messages.append(msg)
        emit({"step":step+1,"type":"assistant","content":msg.get("content",""),"tool_calls":msg.get("tool_calls",[])})
        calls=msg.get("tool_calls") or []
        if not calls: return {"status":"completed","events":events,"messages":messages}
        for call in calls:
            fn=call.get("function",{}); name=fn.get("name"); args=fn.get("arguments") or {}
            if isinstance(args,str): args=json.loads(args)
            try: result=tools.call(name,args)
            except Exception as e: result={"error":type(e).__name__,"message":str(e)}
            emit({"step":step+1,"type":"tool","name":name,"arguments":args,"result":result})
            messages.append({"role":"tool","tool_name":name,"content":json.dumps(result) if not isinstance(result,str) else result})
    return {"status":"max_steps","events":events,"messages":messages}
