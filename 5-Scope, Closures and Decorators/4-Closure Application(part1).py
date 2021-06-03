#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

class Average:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count


a = Average()

print(a.add(10))
print("=====New Code Below=====""")


def average():
    numbers = []

    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count

    return add


c = average()

print(c(10))
print(c.__closure__)
print(c.__code__.co_varnames)

print("=====New Code Below=====""")


def average1():
    total = 0
    count = 0

    def add(number):
        nonlocal total
        nonlocal count
        total = total + number
        count = count + 1
        return total / count

    return add


e = average1()
print(e.__closure__)
print(e.__code__.co_freevars)
print(e(10))
print("=====New Code Below=====""")


class Average1:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, number):
        self.total += number
        self.count += 1
        return self.total / self.count


d = Average1()

print(d.add(10))

print("=====New Code Below=====""")

from time import perf_counter


class Timer:
    def __init__(self):
        self.start = perf_counter()

    def __call__(self):
        return perf_counter() - self.start


t1 = Timer()
print(t1())
t2 = Timer()
print(t2())

print("=====New Code Below=====""")


def timer():
    start = perf_counter()

    def poll():
        return perf_counter() - start

    return poll


x = timer()
print(x())

print("=====New Code Below=====""")

"""" PART 2 """
print("PART 2")


def counter(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        return initial_value

    return inc


counter1 = counter()
print(counter1())
print(counter1())
print("=====New Code Below=====""")


def counter1(fn):
    cnt = 0

    def inner(*arg, **kwargs):
        nonlocal cnt
        cnt += 1
        print(f"{fn.__name__} has been called {cnt} times")
        return fn(*arg, **kwargs)

    return inner


def add(a, b):
    return a + b


def mult(a, b):
    return a * b


counter_add = counter1(add)
counter_mult = counter1(mult)
print(counter_add.__closure__)
print(counter_add.__code__.co_freevars)
print(counter_add(10, 20))

print(counter_mult(2, 5))
print(counter_mult.__closure__)
print(counter_mult.__code__.co_freevars)

print("=====New Code Below=====""")

counters = dict()


def counter2(fn):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)

    return inner


counted_add = counter2(add)
counted_mult = counter2(mult)
print(counted_add(10, 20))
print(counter_mult(2, 5))
