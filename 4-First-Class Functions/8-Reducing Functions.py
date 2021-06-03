#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3

""" Reducing Functions """

# 1: Lets find the maximum value.

l = [5, 8, 6, 10, 9]

_max = lambda x, y: x if x > y else y

print(_max(3, 4))
print("-------------------")
print(10, 2)
print("-------------------")


def _max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result


print(_max_sequence(l))
print("-------------------")

# 2: Lets find the minimum value.

_min = lambda x, y: x if x < y else y


def _min_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result


print(_min_sequence(l))
print("-------------------")

# 3: Lets add values.

_add = lambda x, y: x + y


def _add_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _add(result, x)
    return result


print(_add_sequence(l))
print("-------------------")


# 4:

def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _add(result, x)
    return result


print(_reduce(_max, l))
print("-------------------")

# 5: Lets use the reduce function from Python standard library:

from functools import reduce

reduce(_max, l)
