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

def my_func(a, b=1):
    """ Return a * b"""
    return a * b


# print(help(my_func))

print(my_func.__doc__)


def my_func1(a: 'annotation for a',
             b: 'annotation for b' = 1) -> 'Returns results of a * b':
    """ Documentation for my_func1"""
    return a * b


print(my_func1.__doc__)
print(my_func1.__annotations__)
print()
x = 3
y = 5


def my_func2(a: 'some character', b=max(x, y)) -> f'character a repeated  + {str(max(x, y))} times':
    print(b)
    return a * max(x, y)


print(my_func2('a'))
print(my_func2.__annotations__)
print()


def my_func3(a: int,
             b: 'int > 0 = 1',
             *args: 'some extra positional args',
             k1: 'keyword-only arg 1',
             k2: 'keyword-only arg 2' = 100,
             **kwargs: 'some extra keyword-only args') -> 'return something':
    print(a, b, args, k1, k2, kwargs)


help(my_func3)
print(my_func3.__annotations__)
my_func3(1, 2, 3, 4, 5, k1=10, k3=300, k4=400)
