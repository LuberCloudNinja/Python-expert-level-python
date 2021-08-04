#!/Users/luberlovemagic/opt/anaconda3/bin/python3

""" 1: """


def my_func(a, b, c):
    print(f"a={a}, b={b}, c={c}")


my_func(1, 2, 3)

""" 2: """


def my_func1(a=1, b=2, c=3):
    print(f"a={a}, b={b}, c={c}")


my_func1(10, 20, 30)
my_func1(10, 20)
my_func1(10)
my_func1()

""" 3: """


def my_func2(a, b=2, c=3):
    print(f"a={a}, b={b}, c={c}")


my_func2(c=30, b=20, a=10)
my_func2(10, c=30, b=20)
my_func2(10, c=30)
# my_func2()

