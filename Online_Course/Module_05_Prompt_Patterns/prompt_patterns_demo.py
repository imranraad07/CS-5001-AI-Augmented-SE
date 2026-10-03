"""Reusable prompt-pattern builders for an under-specified SE incident."""

INCIDENT = """A Python web service intermittently returns HTTP 502 through a reverse
proxy. The application sometimes responds normally. Proxy logs, application
logs, health checks, resource usage, and timeout values have not been inspected."""

def persona(p: str) -> str:
    return f"Act as a software reliability engineer. Separate evidence from hypotheses.\n\nINCIDENT:\n{p}"

def flipped_interaction(p: str) -> str:
    return f"INCIDENT:\n{p}\n\nBefore proposing a fix, ask for needed evidence one focused question at a time."

def question_refinement(p: str) -> str:
    return f"INCIDENT:\n{p}\n\nRewrite 'Why is this service returning 502 errors?' as a precise diagnostic question. Do not answer it."

def cognitive_verifier(p: str) -> str:
    return f"INCIDENT:\n{p}\n\nBreak the diagnosis into smaller evidence questions. Do not claim a root cause without evidence."

def reflection(p: str) -> str:
    return f"INCIDENT:\n{p}\n\nPropose a diagnostic plan, critique its assumptions and missing evidence, then produce a revised plan."

PATTERNS = {
    "persona": persona,
    "flipped": flipped_interaction,
    "refinement": question_refinement,
    "verifier": cognitive_verifier,
    "reflection": reflection,
}

if __name__ == "__main__":
    for name, builder in PATTERNS.items():
        print(f"\n=== {name.upper()} ===")
        print(builder(INCIDENT))
