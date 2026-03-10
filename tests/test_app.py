import pytest
from app import soma, subtrai, multiplica

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0

def test_subtrai():
    assert subtrai(5, 3) == 2
    assert subtrai(0, 5) == -5

def test_multiplica():
    assert multiplica(2, 3) == 6
    assert multiplica(-2, 3) == -6
