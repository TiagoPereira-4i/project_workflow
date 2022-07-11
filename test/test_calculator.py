import pytest

from src.functions.calculator import *

def test_sum_positive():
    assert sum(1,3) == 4

def test_sum_negative():
    assert sum(1, -2) == -1

def test_division_ok():
    assert divide(6,2) == 3

def test_division_zero():
    with pytest.raises(ValueError):
        divide(1,0)

def test_subtract():
    assert subtract(2, 1) == 1

def test_multiply():
    assert multiply(2, 1) == 2