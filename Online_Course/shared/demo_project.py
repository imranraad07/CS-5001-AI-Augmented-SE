"""Disposable software project used by agent/tool demonstrations."""
from __future__ import annotations
from pathlib import Path
import tempfile, textwrap

CHECKOUT='''def calculate_total(subtotal: float, discount_percent: float = 0) -> float:
    if subtotal < 0:
        raise ValueError("subtotal must be non-negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")
    total = subtotal - discount_percent
    return round(total, 2)
'''
TESTS='''import pytest
from src.checkout import calculate_total

def test_no_discount(): assert calculate_total(80.00) == 80.00
def test_zero_subtotal(): assert calculate_total(0.00, 0) == 0.00
def test_rejects_negative_subtotal():
    with pytest.raises(ValueError): calculate_total(-1.00, 10)
def test_rejects_invalid_discount():
    with pytest.raises(ValueError): calculate_total(100.00, 101)
def test_percentage_discount(): assert calculate_total(80.00, 25) == 60.00
'''
DOCS={
"CONTRIBUTING.md":"Before merge, run unit tests and obtain one code review approval. Do not modify tests merely to make a defect disappear.",
"RUNBOOK.md":"For checkout failures, reproduce the issue, inspect the implementation, make the smallest safe change, and rerun the test suite.",
"OWNERS.md":"The checkout team owns src/checkout.py. Changes to checkout behavior require review.",
}

def create_workspace():
    root=Path(tempfile.mkdtemp(prefix="cs5001_"))
    (root/"src").mkdir(); (root/"tests").mkdir()
    (root/"src"/"__init__.py").write_text("")
    (root/"src"/"checkout.py").write_text(CHECKOUT)
    (root/"tests"/"test_checkout.py").write_text(TESTS)
    for n,t in DOCS.items(): (root/n).write_text(t)
    return root
