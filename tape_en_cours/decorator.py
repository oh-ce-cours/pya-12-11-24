def f(param):
    print("dans f", param)
    return param


def deco(une_fonction):
    def wrapper(**kwargs, *args):
        print("avant")
        res = une_fonction(param, *args)
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
