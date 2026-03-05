# core/state.py
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class AgentState:
    diff: str = ""
    review_summary: str = ""
    plan: str = ""
    draft_type: str = "" # 'issue' or 'pr'
    draft_content: dict = field(default_factory=dict)
    reflection_verdict: str = "PENDING"
    approved: bool = False