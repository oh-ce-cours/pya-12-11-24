from fizzbuzz import traitement_fizz_buzz


def test_multiple_de_trois():
    # arange
    nombre_entre = 3
    attendu = "fizz"

    # act
    resultat = traitement_fizz_buzz(nombre_entre)

    # assert
    assert resultat == attendu
