from pathlib import Path
import sys
COURSE=Path(__file__).resolve().parents[1]
if str(COURSE) not in sys.path: sys.path.insert(0,str(COURSE))
import streamlit as st
from shared.streamlit_common import client_panel
import uuid
from a2a.types import Message, Part, Role, SendMessageRequest
st.set_page_config(page_title="Module 14 · A2A",layout="wide"); st.title("Module 14 · A2A and Agentic Protocols")
client=client_panel(); task=st.text_input("Task for specialist agent","Review the checkout fix and identify verification evidence.")
if st.button("Create real A2A SDK request and execute specialist"):
    msg=Message(role=Role.ROLE_USER,message_id=str(uuid.uuid4()),parts=[Part(text=task)],context_id=str(uuid.uuid4()))
    request=SendMessageRequest(message=msg)
    st.subheader("A2A SDK message object"); st.code(str(request))
    st.subheader("Specialist agent response"); st.markdown(client.generate(task,system="You are a software-review specialist agent. Return findings and required verification evidence."))
st.info("The request is constructed with the official A2A SDK data model. A networked A2A server is the next deployment step; this module does not fake a network exchange.")
