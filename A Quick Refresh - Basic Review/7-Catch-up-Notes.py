# a, b, *c = 10, 20, 'a', 'b'
# print(a)
# print(b)
# print(c)
#
#
# def func1(a, b, *args):
#     print(a)
#     print(b)
#     print(c)
#
#
# print(func1(10, 20))
# func1(10, 20, 1, 2, 3)
#
#
# def avg(a, *args):
#     count = len(args) + 1
#     total = sum(args) + a
#     if count == 0:
#         return 0
#     else:
#         return total / count
#
#
# print(avg(2, 2, 4, 4))
#
#
# def func2(a, b, c, *args):
#     print(a)
#     print(b)
#     print(c)
#     print(*args)
#
#
# l = [10, 20, 30, 40, 50]
# print(func2(*l))
# print()
#
#
# def func3(*args, d):
#     print(args, d)
#
#
# func3(1, 2, 3, d='a')
# func3(d='a')
# print()
#
#
# def func4(*, d):
#     print(d)
#
#
# func4(d=100)
#
#
# def func5(a, b, *, d):
#     print(a, b, d)
#
#
# func5(1, 2, d=3)
#
#
# def func6(a, b=2, *args, d=100):
#     print(a, b, args, d)
#
#
# func6(1, 2, 3, 4, 5)
# print()
#
#
# def func7(a, b=20, *args, d=0, e):
#     print(a, b, args, d, e)
#
#
# func7('a', 1, 2, 3, 4, e=5)
#
# """ ** kwargs """
#
#
# def func8(**others):
#     print(others)
#
#
# func8(a=1, b=2, c=3)
# print()
#
#
# def func10(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# func10(1, 2, 3, a=10, b=11)
# print()
#
#
# def func11(a, b, *, d, **kwargs):
#     print(a)
#     print(b)
#     print(d)
#     print(kwargs)
#
#
# func11(1, 2, d=10, e=11, f=12)
# print()
#
# """ Putting it al together: """
#
#
# def func12(a, b, *args):
#     print(a, b, args)
#
#
# func12(1, 2, 'x', 'y', 'z')
# print()
#
#
# def func13(a, b, *args, c=10, d=20, **kwargs):
#     print(a, b, args, c, d, kwargs)
#
#
# func13(1, 2, 'x', 'y', 'z', c=100, d=200, x=0.1, y=0.2)
# print()
#
#
# def calc_hi_low_avg(*args, log_to_console=False):
#     hi = int(bool(args)) and max(args)
#     lo = min(args) if len(args) > 0 else 0
#     avg = (hi + lo) / 2
#     if log_to_console:
#         print(f"high={hi}, low={lo},avg={avg}")
#     return avg
#
#
# is_debug = True
# print(calc_hi_low_avg(1, 2, 3, 4, 5, log_to_console=is_debug))
# print()
#
# """ Application: A Simple Function: """
#
# import time
#
#
# def time_it(fn, *args, rep=1, **kwargs):
#     start = time.perf_counter()
#     for num, i in enumerate(range(rep), start=1):
#         fn(num, *args, **kwargs)
#     end = time.perf_counter()
#     return (end - start) / rep
#
#
# print(time_it(print, 1, 2, 3, sep=' -', end=' ***\n', rep=5))
# print()
#
#
# def computer_powers_1(n, *, start=1, end):
#     # using a for loop
#     results = []
#     for i in range(start, end):
#         results.append(n ** i)
#     return results
#
#
# print(computer_powers_1(2, end=5))
#
#
# def computer_powers_2(n, *, start=1, end):
#     # using a list comprehension
#     results = [n ** i for i in range(start, end)]
#     return results
#
#
# print(computer_powers_2(2, end=5))
# print()
#
#
# def computer_powers_3(n, *, start=1, end):
#     # using generator expression
#     return list((n ** i for i in range(start, end)))
#
#
# print(computer_powers_3(2, end=5))
# print()
#
# """ Parameter Defaults - Beware! """
# from datetime import datetime
#
#
# def log(msg, *, dt=None):
#     # if dt is None:
#     #     dt = datetime.utcnow()
#     #     print(f"{dt}, {msg}")
#     # else:
#     #     print(f"{dt}, {msg}")
#     # OR:
#     dt = dt or datetime.utcnow()
#     return dt
#
#
# print(log('message1'))
# print()
#
# my_tuple = (1, 2, 3)
#
#
# def func14(a=my_tuple):
#     print(a)
#
#
# func14()
# print()
#
# """ Parameter Defaults - Beware Again! """
#
#
# def add_item(name: str, quantity: int, unit=1, grocery_list=None):
#     if not grocery_list:
#         grocery_list = []
#     grocery_list.append(f"{name}, {quantity}, {unit}")
#     return grocery_list
#
#
# store1 = add_item('banana', 2, 'units')
# add_item('milk', 1, 'liter', store1)
# print(store1)
# store2 = add_item('python', 1, 'medium-rare')
# print(store2)
# print(store1 is store2)
# print()


# def factorial(n):
#     if n < 1:
#         return 1
#     else:
#         print(f'calculating {n}!')
#         return n * factorial(n - 1)
#
#
# factorial(3)
# factorial(3)

#
# def factorial1(n, *, cache):
#     if n < 1:
#         return 1
#     elif n in cache:
#         return cache[n]
#     else:
#         print(f'calculating {n}!')
#         result = n * factorial1(n - 1, cache=cache)
#         cache[n] = result
#
#
# cache = {}
# factorial1(3, cache=cache)

""" Docstrings and Annotations: """

# print(help(int))
# print()
# print()
# print(help(print))
#
# def my_func(a, b=1):
#     """ Return a * b"""
#     return a * b
#
#
# # print(help(my_func))
#
# print(my_func.__doc__)
#
#
# def my_func1(a: 'annotation for a',
#              b: 'annotation for b' = 1) -> 'Returns results of a * b':
#     """ Documentation for my_func1"""
#     return a * b
#
#
# print(my_func1.__doc__)
# print(my_func1.__annotations__)
# print()
# x = 3
# y = 5
#
#
# def my_func2(a: 'some character', b=max(x, y)) -> f'character a repeated  + {str(max(x, y))} times':
#     print(b)
#     return a * max(x, y)
#
#
# print(my_func2('a'))
# print(my_func2.__annotations__)
# print()
#
#
# def my_func3(a: int,
#              b: 'int > 0 = 1',
#              *args: 'some extra positional args',
#              k1: 'keyword-only arg 1',
#              k2: 'keyword-only arg 2' = 100,
#              **kwargs: 'some extra keyword-only args') -> 'return something':
#     print(a, b, args, k1, k2, kwargs)
#
#
# help(my_func3)
# print(my_func3.__annotations__)
# my_func3(1, 2, 3, 4, 5, k1=10, k3=300, k4=400)
import inspect

""" lambda Expressions: """

# my_func1 = lambda x, y: x ** 2 // y
# print(type(my_func1))
# print(my_func1(2, 2))
#
# a = lambda x: x ** 2
# print(a(2))
#
# b = lambda x, y=10: x + y
# print(b(10))
#
# c = lambda x=10, *args, y=20, **kwargs: (x, args, y, kwargs)
# print(c(10, 30, 40, y=30, a=50, b=60))
# print()
#
#
# def apply_func(x, fn):
#     return fn(x)
#
#
# print(apply_func(3, lambda x: x ** 2))
# print()
#
#
# def apply_func(fn, *args, **kwargs):
#     return fn(*args, **kwargs)
#
#
# print(apply_func(lambda x: x ** 2, 4))
#
# print(apply_func(lambda x, y: x + y, 1, 2))
# print(apply_func(lambda x, *, y: x + y, 1, y=20))
# print(apply_func(lambda *args: sum(args), 1, 2, 3, 4, 5))
# print()

""" Lambda and Sorting: """

# l = [1, 5, 4, 10, 9, 6]
#
# print(sorted(l))
#
# l = ['c', 'B', 'D', 'a']
# print(sorted(l))
#
# print(sorted(l, key=lambda s: s.upper()))
#
# d = {'def': 300, 'abc': 200, 'ghi': 100}
#
# print(sorted(d, key=lambda e: d[e]))
#
#
# def dist_sq(x):
#     return (x.real) ** 2 + (x.imag) ** 2
#
#
# print(dist_sq(1 + 1j))
# print()
#
# l = [3 + 3j, 1 - 1j, 0, 3 + 0j]
#
# print(sorted(l, key=dist_sq))
# print()
# print(sorted(l, key=lambda x: (x.real) ** 2 + (x.imag) ** 2))

""" Functions Introspection """


# TODO: Fix this function
def my_func(a: "mandatory positional",
            b: "optional positional " = 1,
            c=2,
            *args: "add extra positional",
            kw1,
            kw2=100,
            kw3=200,
            **kwargs: "provide extra keyword-only here") -> 'returns i+j':
    """ This function does nothing but does have various parameters and annotations."""
    i = 10
    j = 20
    a = i + j
    return a


print(my_func.__doc__)
print(my_func.__annotations__)
my_func.short_description = "This is a function that does nothing much."
print(my_func.short_description)

print(dir(my_func))

print(my_func.__name__)
print(id(my_func))


def func_call(f):
    print(id(f))
    print(f.__name__)


func_call(my_func)

print(my_func.__defaults__)
print(my_func.__kwdefaults__)
print()
print(dir(my_func.__code__))
print()
print(my_func.__code__.co_varnames)

from inspect import isfunction, ismethod, isroutine

a = 10
print(isfunction(a))
print()
print(isfunction(my_func))
print()
print(ismethod(my_func))
print()


class MyClass:
    def f(self):
        pass


print(isfunction(MyClass.f))
print(ismethod((MyClass.f)))
print()
my_obj = MyClass()
print(isfunction(my_obj.f))
print(ismethod((my_obj.f)))
print()

print(inspect.getsource(my_func))
print()
print(inspect.getmodule(my_func))
print()
print(inspect.getcomments(my_func))
print()
print(inspect.signature(my_func))
print()
print(dir(inspect.signature(my_func)))
print()
sig = inspect.signature(my_func)
print(sig.parameters)
print()
for num, (k, v) in enumerate(sig.parameters.items(), start=1):
    print(f" {num}- {k} {v}")
print()
""" Callables: """
print(callable(print))
result = print('hello')
print(result)
print()
l = [1, 2, 3]
print(callable(l.append))
print()

from decimal import Decimal


class MyClass:
    def __init__(self, x=0):
        print('initializing...')
        self.counter = x

    def __call__(self, x=1):
        print('updating counter...')
        self.counter += x


print(callable(MyClass))
print()
a = MyClass()
print(MyClass.__call__(a, 10))
print()
""" Map, Filer and Zip"""


def fact(n):
    return 1 if n < 2 else n * fact(n - 1)


print(fact(3))

fact_1 = lambda n: 1 if n < 2 else n * fact(n - 1)
print(fact_1(4))

results = list(map(fact_1, range(6)))
print(results)

for x in results:
    print(x)

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]
l3 = 100, 200, 300, 400
results = list(map(lambda x, y, z: (x + y + z), l1, l2, l3))
print(results)
print()
x = range(25)
print(x)
for i in x:
    print(i)
print()
print(list(filter(lambda x: x % 3 == 0, range(25))))
print()

l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]
l3 = 'python'
results = zip(l1, l2, l3)
for x in results:
    print(*x)

print(list(zip(l1, l2, l3)))

print(list(zip(range(10000), 'python')))
print()

l = range(10)
print(list(l))

results = [fact(n) for n in range(10)]
print(results)

results = (fact(n) for n in range(10))
for x in results:
    print(x)

results = list((fact(n) for n in range(10)))
print(results)

l1 = [1, 2, 3, 4, 5, 6]
l2 = [10, 20, 30, 40]
print(list(map(lambda x, y: (x + y), l1, l2)))
results = [x + y for (x, y) in zip(l1, l2)]
print(results)
results = list(filter(lambda x: x % 2 == 0, (map(lambda x, y: (x + y), l1, l2))))
print(results)
results = [x + y for x, y in zip(l1, l2) if (x + y) % 2 == 0]

results = [fact(i) for i in range(0, 10)]
print(results)

l1 = [1, 2, 3, 4, 5, 6, ]
l2 = [10, 20, 30, 40]

results = [x + y for x, y in zip(l1, l2) if (x + y) % 2 == 0]

print(results)

l = [5, 8, 6, 10, 9]

_max = lambda x, y: x if x > y else y
_min = lambda x, y: x if x < y else y


def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result


def min_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result


print(max_sequence(l))
print(min_sequence(l))

_add = lambda a, b: a + b


def add_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _add(result, x)
    return result


print(add_sequence(l))


def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result


print(_reduce(_add, l))
print(_reduce(_max, l))
print(_reduce(_min, l))
print()

from functools import reduce

print(reduce(_max, l))
print(reduce(_add, l))
print(reduce(_min, l))
print()
s = {True, 1, 0, None}
print(all(s))
s2 = {True, 1, "s"}
print(all(s2))
print()
print(reduce(lambda a, b: bool(a) and bool(b), s))
print()
""" Partial Functions: """

from functools import partial


def my_func(a, b, c):
    print(a, b, c)


my_func(10, 20, 30)


def f(x, y):
    return my_func(10, x, y)


f(20, 30)
f(100, 200)

f = lambda x, y: my_func(10, x, y)
f(300, 400)
print()

f = partial(my_func, 10)
f(20, 30)
f = partial(my_func, 10, 20)
f(30)
print()


def my_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)


my_func(10, 20, 100, 200, k1='a', k2='b', k3=1000, k4=2000)


def f(x, *vars, kw, **kwvars):
    return my_func(10, x, *vars, k1='a', k2=kw, **kwvars)


f(20, 100, 200, kw='b', k3=1000, k4=4000)

f = partial(my_func, 10, k1='a')
f(20, 100, 200, k2='b', k3=1000, k4=2000)
print()


def pow(base, exponent):
    return base ** exponent


sq = partial(pow, exponent=2)
print(sq(5))


def my_func(a, b):
    print(a, b)


a = [1, 2]
f = partial(my_func, *a)
f()
print()
origin = (0, 0)
t_1 = 1, 0, -3, 0, 10
t_2 = 1, 2, 2, 0, 10
l = list(zip(t_1, t_2))
print(l)

print(sorted(l))
print()

""" The Operator Module: """

import operator

for attributes in dir(operator):
    print(attributes)

print()

print(operator.add(1, 2))
print(operator.mul(2, 3))
print(operator.truediv(3, 2))
print(operator.floordiv(13, 2))

from functools import reduce

print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))

print(reduce(operator.mul, [1, 2, 3, 4]))
print()

my_list = [1, 2, 3, 4]
print(operator.getitem(my_list, 1))
my_list[1] = 100
print(operator.getitem(my_list, 1))
del my_list[3]
print(my_list)


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self, c, d, *, e):
        print('test method running....!',
              (self.a, self.b, c, d, e))


obj = MyClass()
f = operator.attrgetter('a', 'b', 'c')
print(f(obj))
# or
print(operator.attrgetter('a', 'b', 'c')(obj))
print()
f = operator.attrgetter('test')(obj)
print(f(100, 200, e=300))
print()
print()

""" Scopes, Closures and Decorators: """

a = 10


def my_func(n):
    c = n ** 2
    return c


def my_func1(n):
    print('global a:', a)
    c = a ** n
    return c


print(my_func1(2))
print()
print()

""" Nonlocal Scopes: """


def outer_func():
    x = 'hello'

    def inner_func():
        print(x)

    inner_func()


def outer_func1():
    x = 'hello'

    def inner1():
        def inner2():
            print("inner2", x)

        inner2()

    inner1()


outer_func1()
print()


def outer_func2():
    x = 'hello'

    def inner():
        x = 'python'
        print('inner:', x)

    inner()
    print('outer:', x)


outer_func2()
print()

x = 'global'


def outer_func3():
    global x
    x = 'monty'

    def inner():
        global x
        x = 'python'
        print('inner:', x)

    inner()
    print('outer:', x)


outer_func3()
print('global:', x)
print()
print()

""" Closures: """


def outer1():
    x = 'python'

    def inner():
        print(x)
        print(hex(id(x)))

    return inner


fn = outer1()
print(fn.__code__.co_freevars)  # Check for free variables.
print(fn.__closure__)
print(fn())
print()
print()


def outer2():
    x = [1, 2, 3]
    print(hex(id(x)))

    def inner():
        y = x
        print(hex(id(x)))

    return inner()


outer2()
print(outer2.__closure__)
print()
print()


def outer3():
    count = 0
    print(hex(id(count)))

    def inc():
        nonlocal count
        count += 1
        print(hex(id(count)))
        return count

    return inc


fn = outer3()
print(fn())
print(fn.__code__.co_freevars)
print(fn.__closure__)
print(hex(id(0)))
print()
print()


def outer4():
    count = 0

    def inc1():
        nonlocal count
        count += 1
        return count

    def inc2():
        nonlocal count
        count += 1
        return count

    return inc1, inc2


fn1, fn2 = outer4()
print(fn1.__code__.co_freevars)
print(fn2.__code__.co_freevars)
print(fn1.__closure__)
print(fn2.__closure__)
print()
print()


def pow(n):
    def inner(x):
        return x ** n

    return inner


square = pow(5)
print(square.__closure__)
print(hex(id(2)))

cube = pow(3)


def adder(n):
    def inner(x):
        return x + n

    return inner


add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)

print(add_1.__code__.co_freevars)
print(add_1.__closure__, add_2.__closure__, add_3.__closure__)
print()
print()
print(add_1(10))
print(add_2(10))
print(add_3(10))

adders = []

for n in range(1, 4):
    adders.append(lambda x: x + n)
print(adders)
print()
print()


def create_adders():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x: x + n)
    return adders


adders = create_adders()
print(adders)
print()
print()


def outer():
    x = 'python'

    def inner():
        print(hex(id(x)))

    return inner


fn = outer()
fn()
print(fn.__closure__)
print(fn.__code__.co_freevars)
print()
print()


def outer():
    x = [1, 2, 3]
    print(hex(id(x)))
    print(fn.__closure__)

    def inner():
        y = x
        print(hex(id(y)))
        print(fn.__closure__)

    return inner()


outer()


def outer():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count

    return inc()


fn = outer()
print(fn.__code__.co_freevars)

""" First-Class Objects """
