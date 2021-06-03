#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

# 1:

def outer_func():
    x = 'hello'

    def inner_func():
        print(x)

    inner_func()


outer_func()
print("-------------------")


# 2:

def outer_func1():
    x = 'hello'

    def inner1():
        def inner2():
            print(x)

        inner2()

    inner1()


outer_func1()
print("-------------------")


# 3:

def outer_func2():
    x = 'hello'

    def inner():
        x = 'python'
        print('inner', x)

    inner()
    print('outer:', x)


outer_func2()
print("-------------------")


# 4:

def outer_func3():
    x = 'hello'

    def inner():
        nonlocal x
        x = 'python'
        print('inner', x)

    print('outer(before)', x)
    inner()
    print('outer:', x)


outer_func3()
print("-------------------")


# 5:

def outer():
    x = 'hello'

    def inner1():
        def inner2():
            nonlocal x
            x = 'python'

        inner2()

    inner1()
    print(x)


outer()
print("-------------------")


# 6:

def outer1():
    x = 'hello'

    def inner1():
        nonlocal x
        x = 'python'

        def inner2():
            nonlocal x
            x = 'monty'

        inner2()

    inner1()
    print(x)


outer1()
print("-------------------")

# 7:
x = 'python'


def outer3():
    # global x
    x = 'monty'

    def inner():
        nonlocal x
        x = 'hello'

    print(x)
    inner()
    print(x)


outer3()
print(x)