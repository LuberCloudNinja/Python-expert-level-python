#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

def outer():
    x = 'python'

    def inner():
        print(x)

    return inner


fn = outer()
fn()
print(fn.__code__.co_freevars)

print(fn.__closure__)
print("=====New Code Below=====""")


def outer1():
    x = [1, 2, 3]
    print(hex(id(x)))

    def inner():
        y = x
        print(hex(id(y)))

    return inner


fn1 = outer1()

fn1()
print(fn1.__closure__)
print("=====New Code Below=====""")


def outer2():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment()


fn2 = outer2()
print(fn2)
print("=====New Code Below=====""")


def outer3():
    count = 1

    def increment1():
        nonlocal count
        count += 1
        return count

    def increment2():
        nonlocal count
        count += 1
        return count

    return increment1, increment2


fn3, fn4 = outer3()
print(fn3.__closure__, fn4.__closure__)
print(fn3.__code__.co_freevars, fn4.__code__.co_freevars)
print(fn3(), fn4())

print("=====New Code Below=====""")

adders = []


def create_adders():
    for n in range(1, 4):
        adders.append(lambda x: x + n)
    return adders


print(create_adders())
print(adders[0].__closure__)
print(adders[1].__closure__)
print(adders[0].__code__)
