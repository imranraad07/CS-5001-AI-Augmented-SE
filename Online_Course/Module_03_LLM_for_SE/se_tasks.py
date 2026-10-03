"""Module 3 software-engineering artifact."""

def normalize_username(username: str) -> str:
    """Trim whitespace, normalize case, and reject an empty username."""
    normalized = username.strip()
    if not normalized:
        raise ValueError("username must not be empty")
    # Intentional demo bug: case normalization is missing.
    return normalized
