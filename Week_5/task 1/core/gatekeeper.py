import sys
from typing import Dict, Any

class Gatekeeper:
    def __init__(self, model_client):
        self.model = model_client  # e.g., Ollama client from your project

    def reflect(self, draft: Dict[str, str], diff_context: str) -> Dict[str, Any]:
        """
        The Reflection Pattern: Audit the draft for hallucinations or missing info.
        """
        print("[Gatekeeper] Performing Reflection/Audit...")
        
        reflection_prompt = f"""
        Critique the following GitHub draft based on the provided Git Diff.
        
        GIT DIFF:
        {diff_context}
        
        PROPOSED DRAFT:
        Title: {draft.get('title')}
        Body: {draft.get('body')}
        
        RULES:
        1. Does the draft mention files NOT present in the diff? (Hallucination check)
        2. Does it include a 'Test Plan'?
        3. Is the 'Risk Level' justified by the complexity of the diff?
        4. Are there any unsupported claims?
        
        Output a JSON-style verdict:
        {{
            "status": "PASS" or "FAIL",
            "reason": "Explain why it failed or why it is high quality",
            "required_changes": ["list", "of", "fixes"]
        }}
        """
        
        # Call your local Ollama/LLM
        verdict_raw = self.model.generate(reflection_prompt)
        # Parse logic here (simplifying for the example)
        return verdict_raw

    def request_human_approval(self, draft: Dict[str, str]) -> bool:
        """
        The Final Gate: Human-in-the-loop validation.
        """
        print("\n" + "="*50)
        print("FINAL DRAFT FOR REVIEW:")
        print(f"TITLE: {draft.get('title')}")
        print(f"BODY:\n{draft.get('body')}")
        print("="*50)
        
        user_input = input("\n[Gatekeeper] Approve creation on GitHub? (y/n): ").lower()
        
        if user_input == 'y':
            print("[Gatekeeper] Approval granted. Proceeding to Tool Use...")
            return True
        else:
            print("[Gatekeeper] Action aborted by user. No changes made.")
            return False