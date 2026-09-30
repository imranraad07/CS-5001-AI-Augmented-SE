import pytest

from src.checkout import calculate_total


def test_no_discount():
    assert calculate_total(80.00) == 80.00


def test_zero_subtotal():
    assert calculate_total(0.00, 0) == 0.00


def test_rejects_negative_subtotal():
    with pytest.raises(ValueError):
        calculate_total(-1.00, 10)


def test_rejects_invalid_discount():
    with pytest.raises(ValueError):
        calculate_total(100.00, 101)


def test_percentage_discount():
    assert calculate_total(80.00, 25) == 60.00
