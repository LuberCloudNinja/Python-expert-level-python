#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3


""" Global and Local Scopes """

# 1:

a = 10
print(a)
print("-------------------")


def my_func(n):
    c = n ** 2
    return c


print(my_func(a))
print("-------------------")


# 2:

def my_func1(n):
    print('global a:', a)
    c = a ** n
    return c


print(my_func1(2))
print("-------------------")


# 3:
def my_func2(n):
    a = 20
    c = a ** n
    return c


print(my_func2(2))
print("-------------------")


# 4: Using global scope inside a function:

def my_func3(n):
    global a
    a = 20  # Object a will change in the module scope because we made it global and then assigned a new value
    c = a ** n
    return c


print(my_func3(2))
print(a)
print("-------------------")


# 5:

def my_func4():
    global var
    var = 'hello world'


print(my_func4())
print(var)
print("-------------------")

# 6:
b = 10


def my_func5():
    global b
    b = 'hello'
    print('global b:', b)


my_func5()
print(b)
print("-------------------")

# 7:
c = 10
f = lambda n: print(c ** n)
f(2)
print("-------------------")

# 8:
