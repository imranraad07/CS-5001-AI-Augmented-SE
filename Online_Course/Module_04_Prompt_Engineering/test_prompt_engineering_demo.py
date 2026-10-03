from prompt_engineering_demo import weak_prompt, engineered_prompt

def test_weak_is_underspecified():
    assert "CONSTRAINTS" not in weak_prompt()

def test_engineered_has_structure():
    prompt = engineered_prompt()
    for section in ("CONTEXT", "TASK", "CONSTRAINTS", "EXPECTED OUTPUT", "VERIFICATION"):
        assert section in prompt
