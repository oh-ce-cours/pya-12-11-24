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
    match nombre:
        case nombre % 3==0 and nombre % 5 == 0: 
            print("fizzbuzz")
        case ... :  
            print("fizz")
        case ...:
            print("buzz")
        case ...:
            print(nombre)