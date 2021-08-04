#!/Users/luberlovemagic/opt/anaconda3/bin/python3
import time

""" Let's create a function that will measure the time it takes a function to run"""

""" 1: """


def time_it1(fn, *args, **kwargs):
    print(args, kwargs)


time_it1(print, 1, 2, 3, sep=' - ', end=' ***')
print('===================')
print('===================')

""" 2: """


def time_it2(fn, *args, rep=1, **kwargs):
    for i in range(rep):
        fn(*args, **kwargs)


time_it2(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=5)
print('===================')
print('===================')

""" 3: Let's create the same function but with a timer"""


def time_it3(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    total = (start - end) / rep
    print(total)


time_it3(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=5)
print('===================')
print('===================')

""" 4: We'll calculate the power of n (n**of) """


def compute_powers_1(n, *, start=1, end):
    # Using a for loop
    results = []
    for i in range(start, end):
        print(i)
        results.append(n ** i)
    return results


print(compute_powers_1(2, end=5))
print('===================')
print('===================')

""" 5: Same as above but using list comprehension """


def compute_powers_2(n, *, start=1, end):
    # Using a list comprehension
    return [n ** i for i in range(start, end)]


print(compute_powers_2(2, end=5))
print('===================')
print('===================')
""" 6: Same as above but using generators expression """


def compute_powers_3(n, *, start=1, end):
    # Using generators expression
    # Attention with the below, the difference with the above example is the brackets.
    return (n ** i for i in range(start, end))


print(list(compute_powers_3(2, end=5)))
print('===================')

# Lets time it now using the time_it1 function previously created:
time_it3(compute_powers_1, 2, start=0, end=20000, rep=5)
time_it3(compute_powers_2, 2, start=0, end=20000, rep=5)
time_it3(compute_powers_3, n=2, start=0, end=20000, rep=5)

# Outside of the scope of this, let' understand a bit about generators expression:

a = (2 ** i for i in range(5))
print(a)
# We could print out this generator as a list:
print(list(a))


