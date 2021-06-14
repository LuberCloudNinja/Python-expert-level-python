""" Variable Equality """


def func_1():
    a = 10
    b = 10
    print(id(a))
    print(id(b))
    print("a is b: ", a is b)
    print("a == b: ", a == b)


def func_2():
    a = 500
    b = 500
    print(id(a))
    print(id(b))
    print("a is b: ", a is b)
    print("a == b: ", a == b)


def func_3():
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(id(a))
    print(id(b))
    print("a is b: ", a is b)
    print("a == b: ", a == b)


def func_4():
    a = 10
    b = 10.0
    print(id(a))
    print(id(b))
    print("a is b: ", a is b)
    print("a == b: ", a == b)


func_1()
print()
func_2()
print()
func_3()
print()
func_4()
