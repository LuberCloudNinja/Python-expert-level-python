#!/Users/luberlovemagic/opt/anaconda3/bin/python3

""" 1: Lambda Expressions """


def sq(x):
    return x ** 2


""" Now we're creating it as a Lambda expression: """

f = lambda x: x ** 2

g = lambda x, y=10: x + y

print(g(10))
# or
print(g(10, 20))

""" 2: """
e = lambda x, *args, y, **kwargs: (x, *args, y, kwargs)

print(e(1, 'a', 'b', y=100, a=10, b=20))

print("-------------------")
print("-------------------")

""" 3: """


def apply_func1(x, fn):
    return fn(x)


# Remember that the "sq" object was created it in exercise 1 (above) as a function:


print(apply_func1(5, sq))

# Now the same as above but using a Lambda Expression:

print(apply_func1(5, lambda x: x ** 2))
print(apply_func1(5, lambda x: x ** 3))

""" 4: """


def apply_func2(fn, *args, **kwargs):
    return fn(*args, **kwargs)


print(apply_func2(sq, 3))

# or

print(apply_func2(lambda x: x ** 2, 3))

# Another way to use Lambda Express:

print(apply_func2(lambda x, y: x + y, 1, 2))

# or

print(apply_func2(lambda x, *, y: x + y, 1, y=20))
# or

print(apply_func2(lambda *args: sum(args), 1, 2, 3, 4, 5))


