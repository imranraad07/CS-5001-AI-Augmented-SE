import pytest
from se_tasks import normalize_username

def test_trims_and_normalizes():
    assert normalize_username("  Alice  ") == "alice"

def test_normalizes_case():
    assert normalize_username("ALICE") == "alice"

def test_rejects_empty():
    with pytest.raises(ValueError):
        normalize_username("   ")
