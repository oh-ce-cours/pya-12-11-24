from fizzbuzz import traitement_fizz_buzz


def test_fizzbuzz_3_est_fizz(capfd):
    # arange
    nombre_entre = 3
    attendu = "fizz"

    # act
    traitement_fizz_buzz(nombre_entre)
    resultat = capfd.readouterr().out

    # assert
    assert "fizz" in resultat


def test_fizzbuzz_99_est_fizz():
    # arange
    nombre_entre = 99
    attendu = "fizz"

    # act
    resultat = traitement_fizz_buzz(nombre_entre)

    # assert
    assert resultat == attendu
