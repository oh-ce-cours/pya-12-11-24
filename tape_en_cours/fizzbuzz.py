# for nombre in range(1, 101):
#     if nombre % 3 == 0 and nombre % 5 == 0:
#         print("fizzbuzz")
#     elif nombre % 3 == 0:
#         print("fizz")
#     elif nombre % 5 == 0:
#         print("buzz")
#     else:
#         print(nombre)

for nombre in range(1, 101):
    match (nombre % 3, nombre % 5):
        case (0, 0):
            print("fizzbuzz")
        case (0, _):
            print("fizz")
        case (_, 0):
            print("buzz")
        case (_, _):
            print(nombre)
