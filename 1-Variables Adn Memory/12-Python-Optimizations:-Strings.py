#!/Users/luberlovemagic/opt/anaconda3/bin/python3
import sys
import time

""" 1: """

a = 'hello'
b = 'hello'

print(id(a), id(b))
a = 'hello world'
b = 'hello world'

print(id(a), id(b))

a = sys.intern('hello world')
b = sys.intern('hello world')
c = 'hello world'
print(id(a), id(b), id(c))


def compare_using_equals(n):
    a = 'a long string that is not interned' * 200
    b = 'a long string that is not interned' * 200
    for i in range(n):
        if a == b:
            pass


def compare_using_interning(n):
    a = sys.intern('a long string that is not interned' * 200)
    b = sys.intern('a long string that is not interned' * 200)
    for i in range(n):
        if a is b:
            pass


# Now, we'll be calling each function to see which output is the fastest between the equal logical operator in the
# loop 'if a == b' or using the 'is' in the second function.
start = time.perf_counter()
compare_using_equals(10000000)
end = time.perf_counter()
print('equality', end - start)

start = time.perf_counter()
compare_using_interning(10000000)
end = time.perf_counter()
print('equality', end - start)

