import pytest
from src.prime_checker import is_prime

def test_is_prime_with_prime_numbers():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(7) is True
    assert is_prime(11) is True
    assert is_prime(13) is True
    assert is_prime(17) is True
    assert is_prime(19) is True
    assert is_prime(23) is True
    assert is_prime(29) is True

def test_is_prime_with_non_prime_numbers():
    assert is_prime(4) is False
    assert is_prime(6) is False
    assert is_prime(8) is False
    assert is_prime(9) is False
    assert is_prime(10) is False
    assert is_prime(12) is False
    assert is_prime(15) is False
    assert is_prime(21) is False
    assert is_prime(25) is False
    assert is_prime(27) is False

def test_is_prime_with_edge_cases():
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-1) is False
    assert is_prime(-5) is False

def test_is_prime_with_large_prime():
    assert is_prime(7919) is True

def test_is_prime_with_large_non_prime():
    assert is_prime(10000) is False

def test_is_prime_raises_value_error_for_n_less_than_2():
    with pytest.raises(ValueError):
        is_prime(1)
    with pytest.raises(ValueError):
        is_prime(0)
    with pytest.raises(ValueError):
        is_prime(-1)
    with pytest.raises(ValueError):
        is_prime(-10)
