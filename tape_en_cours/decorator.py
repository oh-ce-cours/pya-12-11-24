def f(param):
    print("dans f", param)
    return param


def deco(une_fonction):
    def wrapper(param):
        print("avant")
        res = une_fonction(param)
        print("apres")
        return res

    return wrapper


def g():
    print("dans g")


print(f)
f = deco(f)
print(f)
print(f("toto"))
