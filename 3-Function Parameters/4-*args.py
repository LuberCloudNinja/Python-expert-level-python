#!/Users/luberlovemagic/opt/anaconda3/bin/python3

""" 1: """
a, b, *c = 10, 20, 'a', 'b'
print(a, b, c)
print('=================')
l = a, b, *c


def func1(a, b, *args):
    print(a)
    print(b)
    print(args)


func1(10, 20)
print('=================')
func1(*l)
func1(1, 2, 3, 4, 5, 6, 7, 8, 9)

print('=================')


# 2:

def avg(*args):
    count = len(args)
    total = sum(args)
    if total == 0:
        return 0
    return total / count


print(avg(2, 2, 4, 4))
print(avg())
print('=================')


# 2: Another way to do the same:

def avg1(*args):
    count = len(args)
    total = sum(args)
    return count and total / count


print(avg1(2, 2, 4, 4))
print(avg1())
print('=================')


# 3: If you want the user to enter an argument, we can do it the following way:

def avg2(a, *args):
    count = len(args) + 1
    total = sum(args) + a
    return total / count


print(avg2(2, 2, 4, 4))
print(avg2(2))  # We must enter an argument when calling the function.
print('=================')


# 4:

def func3(a, b, c):
    print(a)
    print(b)
    print(c)


l = [10, 20, 30]
func3(*l)
