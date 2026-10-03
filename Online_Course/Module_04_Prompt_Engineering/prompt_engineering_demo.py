"""Generate weak and engineered prompts for the same SE task."""
from textwrap import dedent

BUGGY_CODE = """def calculate_total(subtotal, discount_percent=0):
    total = subtotal - discount_percent
    return round(total, 2)
"""

def weak_prompt() -> str:
    return f"Fix this code.\n\n{BUGGY_CODE}"

def engineered_prompt() -> str:
    return dedent(f"""
    CONTEXT
    A checkout function interprets discount_percent as a percentage.
    A test expects calculate_total(80.00, 25) to return 60.00.

    TASK
    Diagnose the implementation and propose the minimum correct change.

    CONSTRAINTS
    - Preserve the public interface.
    - Do not modify the test expectation.
    - Do not add dependencies.
    - Do not invent requirements.

    EXPECTED OUTPUT
    1. State the defect in one sentence.
    2. Show only the corrected calculation.
    3. Explain how the supplied test verifies it.

    VERIFICATION
    The calculation must produce 60.00 for subtotal=80.00 and discount_percent=25.

    CODE
    {BUGGY_CODE}
    """).strip()

if __name__ == "__main__":
    print("=== WEAK PROMPT ===\n" + weak_prompt())
    print("\n=== ENGINEERED PROMPT ===\n" + engineered_prompt())
