from prompt_patterns_demo import INCIDENT, PATTERNS

def test_all_patterns_include_context():
    for builder in PATTERNS.values():
        assert INCIDENT in builder(INCIDENT)

def test_patterns_are_distinct():
    prompts = [builder(INCIDENT) for builder in PATTERNS.values()]
    assert len(prompts) == len(set(prompts))

def test_reflection_requests_critique():
    assert "critique" in PATTERNS["reflection"](INCIDENT).lower()
