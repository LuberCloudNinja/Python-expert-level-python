#!/Users/luberlovemagic/opt/anaconda3/bin/python3

import sys
import time

""" 1: """
# Lets see how much storage space(memory) is used when we create integers:

print(type(100))

# The below method will give us the memory that is being used to store a particular variable/value.

print(sys.getsizeof(0))
print(sys.getsizeof(1))
print(sys.getsizeof(2 ** 1000))
print((160 - 24) * 8)

""" 2: """


def calc(a):
    for i in range(1000000):
        a * 2


start = time.perf_counter()
print(calc((10)))
ends = time.perf_counter()
print(start - ends)

start = time.perf_counter()
print(calc((2**100)))
ends = time.perf_counter()
print(start - ends)
print(2**100)

start = time.perf_counter()
print(calc((2**10000)))
ends = time.perf_counter()
print(start - ends)
print(2**10000)