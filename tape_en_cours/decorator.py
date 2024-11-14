def f(param):
    print("dans f", param)
    return param


def deco(une_fonction):
    print("avant wrapper", une_fonction)

    def wrapper(*args, **kwargs):
        print("dans wrapper", une_fonction)
        print("avant")
        res = une_fonction(*args, **kwargs)
        print("apres")
        return res

    return wrapper


@deco
def g():
    print("dans g")


print(f)
f = deco(f)
print(f)
print(f(param="toto"))
g()
