#!/Users/luberlovemagic/opt/anaconda3/bin/python3

""" 1: """

a = 10
print(type(a))
b = int(10)
print(type(a))
# help(int)

c = int()
print(c)
c = int('101', base=2)
print(c)

""" 1: Functions are objects too """


# 1.1:

def square(a):
    return a ** 2


print(type(square))
f = square
print(id(square))
print(id(f))
print(f is square)
print(square(2))
print(f(2))


# 1.2:

def cube(a):
    return a ** 3


def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube


f = select_function(1)
print(f is square)
print(f(2))

f = select_function(2)
print(f is square)
print(f is cube)
print(f(2))
print(select_function(2)(3))


# 1.3: Functions can be pass to a function too.

def exec_function(fn: "function", n: int):
    return fn(n)


print(exec_function(cube, 3))
print(exec_function(square, 3))

