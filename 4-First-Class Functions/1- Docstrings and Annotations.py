#!/Users/luberlovemagic/opt/anaconda3/bin/python3

""" 1: Docstrings """


def my_func1(a, b=1):
    """ returns a * b

    some additional docs here

    Inputs:

    Outputs"""
    return a * b


print(help(my_func1))
print("-------------------")
print(my_func1.__doc__)
print("-------------------")
print("-------------------")

""" 2: Annotations """


def my_func2(a: "annotation for a",
             b: "annotation for b" = 1) -> "Return Something with a long annotation":
    """ documentation for my_func2"""
    return a * b


print(help(my_func2))
print("-------------------")
print(my_func2.__doc__)
print(my_func2.__annotations__)
print("-------------------")
print("-------------------")

""" 3: """

x = 3
y = 5


def my_func3(a: "some character") -> "character a repeated" + str(max(x, y)):
    return a * max(x, y)


print(my_func3("a"))
print("-------------------")
print(my_func3.__annotations__)
print("-------------------")
print(my_func3.__doc__)
print("-------------------")
print("-------------------")

""" 4: """


def my_fubc4(a: str,
             b: "int > 0" = 1,
             *args: "some extra positional arg 1",
             k1: "keyword-only arg 1",
             k2: "keyword-only arg 2" = 100,
             **kwargs: "some extra keyword-only args") -> " return something":
    print(a, b, args, k1, k2, kwargs)


print(help(my_fubc4))
print(my_fubc4.__annotations__)
my_fubc4(1, 2, 3, 4, 5, k1=10, k3=300, k4=400)

print(hex(id(my_fubc4)))
