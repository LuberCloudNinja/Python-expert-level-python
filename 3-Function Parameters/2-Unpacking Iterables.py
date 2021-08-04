#!/Users/luberlovemagic/opt/anaconda3/bin/python3

""" 1: Tuples """

a = (1, 2, 3)
print(type(a))
a = 1, 2, 3
print(type(a))
a = 1,
b = (1,)
print(type(a))
print(type(b))

# Create an empty tuple:

a = ()
print(type(a))

""" 2: Unpack a list into a tuple """

a, b, c = [1, 'a', 3.14]
print(a)
print(b)
print(c)

# Because the right side of the previous variable is a tuple, we could do it as follow:

(a, b, c) = [1, 'a', 3.14]
print(a)
print(b)
print(c)

# Unpacking a tuple into another tuple:

a, b = (1, 2)
print(a)
print(b)

# or

(a, b) = (1, 2)
print(a)
print(b)

a, b = 10, 20
print(a)
print(b)

a, b, c = 10, 'a', 3.14
print(a)
print(b)
print(c)

a, b, c = 10, {1, 2}, ['a', 'b']
print(a)
print(b)
print(c)

# Swapping values:

a, b = 10, 20
print(a, b)
print(id(a), id(b))
a, b = b, a
print(a, b)
# The above example translates to:
c = (id(b), id(a))
print(c)

""" 3: Unpack Strings """

for e in 'XYZ':
    print(e)

a, b, c = 'XYZ'
print(a)
print(b)
print(c)

""" 4: Unpack Sets and Dictionaries"""
# Sets and dictionaries are un-order data types:

s = {'p', 'y', 't', 'o', 'n'}
print(s)

for e in s:
    print(e)
print('=================')

# Dictionaries:

d = {'a': 1, 'b': 2, 'c': 3}

for e in d:
    print(e)
print('=================')

# Another way to unpack the dictionary:
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
a, b, c, d = d
print(a)
print(b)
print(c)
print(d)

print('=================')
# or:
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d, a, b, c = d

print(d)
print(a)
print(b)
print(c)
print('=================')

# Iterate over the dictionary:

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for e in d:
    print(e)

print('=================')

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
a, b, c, d = d.values()
print(a, b, c, d)

print('=================')

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for num, (keys, values) in enumerate(d.items(), start=1):
    print(f"{num}-{keys}:{values}")


d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
