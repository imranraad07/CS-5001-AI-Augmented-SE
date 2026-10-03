from pathlib import Path
import sys
COURSE=Path(__file__).resolve().parents[1]
if str(COURSE) not in sys.path: sys.path.insert(0,str(COURSE))
import streamlit as st
from shared.streamlit_common import client_panel
from shared.demo_project import CHECKOUT,TESTS
st.set_page_config(page_title="Module 4 · Prompt Engineering",layout="wide"); st.title("Module 4 · Prompt Engineering")
client=client_panel(); weak=st.text_area("Weak prompt","Fix this code.\n\n"+CHECKOUT); strong=st.text_area("Engineered prompt",f"""CONTEXT: Checkout percentage-discount test fails.
IMPLEMENTATION:
{CHECKOUT}
TESTS:
{TESTS}
TASK: Diagnose before changing code.
CONSTRAINTS: Preserve public interface; do not modify tests; no new dependencies; minimum change.
OUTPUT: Root cause, smallest patch, verification required.""")
if st.button("Compare on same Ollama model"):
    a,b=st.columns(2); a.subheader("Weak"); a.markdown(client.generate(weak)); b.subheader("Engineered"); b.markdown(client.generate(strong))
