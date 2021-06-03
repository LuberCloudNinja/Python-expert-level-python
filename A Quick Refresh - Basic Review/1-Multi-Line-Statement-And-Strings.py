a = [1, 2, 3]
a = [1, 2,
     3, 4, 5]

print(a)

a = [1  # item 1
    , 2]
print(a)

a = (1,  # comment
     2  # comment
     , 3)

a = {'key1': 1  # value for key 1
    , 'key2': 2  # value for key 2
     }


def my_func(a,  # this is used to indicate.....
            b  # comment
            , c):
    print(a, b, c)


my_func(10, 20, 30)
my_func(10,
        20,
        30)

my_func(10,  # comment
        20,  # comment
        30  # comment
        )

a = 10
b = 20
c = 30

if a > 5 and b > 10 and c > 20:
    print("Yes")

if a > 5 \
        and b > 10 \
        and c > 20:
    print("Yes")

a = '''This is a string'''
print(a)
a = '''This
is a string'''
print(a)
a = ''' This
 is a string
    that is created over multiple lines'''
print(a)

a = '''Some items:
    1. item 1
    2. item2 '''
print(a)


def my_func():
    a = '''Multi-line string
    that is indented in the second line.'''
    return a


print(my_func())
