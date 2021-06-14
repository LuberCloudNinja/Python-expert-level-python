""" Everything is an Object """


def func_1():
    a = 10
    print(type(a))
    b = int(10)
    print(type(b))
    print("a is b", a is b)
    print("a == b", a == b)
    # print(help(int))


def func_2():
    c = int('101', base=2)
    print(c)


def square(a):
    return a ** 2


def cube(a):
    return a ** 3


def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube


def exec_function(fn, n):
    return fn(n)


func_1()
print()
func_2()
print()
print(type(square))
print()
print()
print(square(2))
print()
print(cube)
print()
f = select_function(1)
print("f is square?: ", f is square)
print(f(2))
f = select_function(2)
print(print("f is cube?: ", f is cube))
print(f(2))
print(select_function(2)(3))
print()
print(exec_function(cube, 3))
print(exec_function(square, 3))
