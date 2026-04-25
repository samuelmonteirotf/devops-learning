import pytest
from app import soma, subtrai, multiplica


def test_soma_positivos():
    assert soma(2, 3) == 5


def test_soma_com_negativos():
    assert soma(-1, 1) == 0
    assert soma(-5, -3) == -8


def test_subtrai_resultado_positivo():
    assert subtrai(5, 3) == 2


def test_subtrai_resultado_negativo():
    assert subtrai(0, 5) == -5


def test_multiplica_positivos():
    assert multiplica(2, 3) == 6


def test_multiplica_por_zero():
    assert multiplica(10, 0) == 0
    assert multiplica(0, 10) == 0


@pytest.mark.parametrize("a, b, esperado", [
    (-2, 3, -6),
    (-2, -3, 6),
    (1, 1, 1),
    (100, 100, 10000),
])
def test_multiplica_varios_casos(a, b, esperado):
    assert multiplica(a, b) == esperado
