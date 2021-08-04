#!/Users/luberlovemagic/opt/anaconda3/bin/python3

""" 1: """


def func1(**others):
    print(others)


func1(a=1, b=2, c=3)
print('=================')


def func2(*args, **kwargs):
    print(args)
    print(kwargs)


func2(1, 2, x=100, y=200)
print('=================')


def func3(a, b, *, d, **kwargs):
    print(a)
    print(b)
    print(d)
    print(kwargs)


func3(1, 2, e=100, y=24, x=34, d=43)
print('=================')


def func4(a, b, **kwargs):
    print(a)
    print(b)
    print(kwargs)


func4(1, 2, x=100, y=200)
print('=================')