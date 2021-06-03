#!/Users/luberlovemagic/opt/anaconda3/bin/python3

""" 1: """


def func1(a, b, c):
    print(a, b, c)


func1(1, c=3, b=2)
# or
func1(c=3, b=2, a=1)
print('=================')


def func2(a, b, *args):
    print(a, b, args)


func2(1, 2, 3, 4)
print('=================')


def func3(a, b, *args, d):
    print(a, b, args, d)


func3(1, 2, 3, 4, d=5)
print('=================')


def func4(*args, d):
    if args == ():
        print(d)
    else:
        print(args, d)


func4(1, 2, 3, 4, d='a')
func4(d='a')
print('=================')


def func5(*, d):
    print(d)


func5(d=100)
print('=================')


def func6(a, b, *, d):
    print(a, b, d)


func6(1, 2, d=3)
print('=================')


def func7(a, b=2, *args, d):
    print(a, b, args, d)


func7(1, 5, 3, 4, d='a')
print('=================')


def func8(a, b: str or int = 20, *args, d: str or int = 0, e):
    if args == ():
        for item1 in (a, b, d, e):
            print(item1)
    else:
        for item2 in (a, b, args, d, e):
            print(item2)


func8(5, 4, 3, 2, 1, e='all engines running')
print('=================')
func8(0, 600, d='good morning', e='python!')
print('=================')
func8(10, 10, e=20)
print('=================')
func8(11, 'm/s', 24, 'mph', d='unladen', e='swallow!')
print('======================================')
