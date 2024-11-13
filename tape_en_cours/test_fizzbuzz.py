from fizzbuzz import traitement_fizz_buzz
import pytest


@pytest.mark.parametrize(
    "nombre_entre, attendu",
    [(3, "fizz"), (5, "buzz"), (15, "fizzbuzz"), (4, "4"), (99, "fizz")],
)
def test_fizzbuzz_3_est_fizz(nombre_entre, attendu):
    # act
    resultat = traitement_fizz_buzz(nombre_entre)

    # assert
    assert resultat == attendu
