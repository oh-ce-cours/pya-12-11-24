for nombre in range(1, 101):
    if nombre % 3 == 0 and nombre % 5 == 0:
        print("fizzbuzz")
    elif nombre % 3 == 0:
        print("fizz")
    elif nombre % 5 == 0:
        print("buzz")
    else:
        print(nombre)
