import math
from math import sqrt

s = [1, 2, 3]
print(len(s))

print(sqrt(100))

print(math.exp(1))
print()
print('***********************')


def func_1():
    print("Running func_1")


func_1()

print()
print('***********************')


def func_2(a: str, b: int):
    return a * b


print(func_2('a', 6))

print()
print('***********************')


def fun_3():
    return func_4()


def func_4():
    return 'running func_4'


print(fun_3())

print()
print('***********************')

my_func = func_4
print(my_func())

print()
print('***********************')

fn1 = lambda x: x ** 2

print(fn1(2))


