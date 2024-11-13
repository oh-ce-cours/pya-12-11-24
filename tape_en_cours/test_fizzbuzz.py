from fizzbuzz import traitement_fizz_buzz
import pytest


@pytest.mark.parametrize("nombre_entre", [3, 99], "attendu", ["fizz", "fizz"])
def test_fizzbuzz_3_est_fizz(nombre_entre):
    # arange
    attendu = "fizz"

    # act
    resultat = traitement_fizz_buzz(nombre_entre)

    # assert
    assert resultat == attendu
