import math
from math import sqrt

s = [1, 2, 3]
print(len(s))

print(sqrt(4))

print(math.pi)
print(math.exp(1))


def func_1():
    print("Running func_1")


func_1()

print("************")


def func_2(a: int, b: int) -> None:
    return a * b


print(func_2(2, 3))
print(func_2('a', 3))
print("************")

print(func_2([1, 2], 3))

print("************")


def func_3():
    return func_4()


def func_4():
    return 'running func_4'


print(func_3())


def func_5():
    return func_6()


def func_6():
    print('running func_6')


print(type(func_5))

my_func = func_4
print(my_func())

fn1 = lambda x: x ** 2
print(fn1(2))
