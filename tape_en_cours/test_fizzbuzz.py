from fizzbuzz import traitement_fizz_buzz
import pytest


@pytest.mark.parametrize(nombre_entre=[3, 99])
def test_fizzbuzz_3_est_fizz():
    # arange
    nombre_entre = 3
    attendu = "fizz"

    # act
    resultat = traitement_fizz_buzz(nombre_entre)

    # assert
    assert resultat == attendu


def test_fizzbuzz_99_est_fizz():
    # arange
    nombre_entre = 99
    attendu = "fizz"

    # act
    resultat = traitement_fizz_buzz(nombre_entre)

    # assert
    assert resultat == attendu
