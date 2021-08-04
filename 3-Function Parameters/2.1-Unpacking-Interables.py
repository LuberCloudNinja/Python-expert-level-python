""" 1: Tuples: """

a = (1, 2, 3)
print(type(a))
print()
a = 1, 2, 3
print(type(a))

""" 2: Unpacking: """
a, b, c = [1, 'a', 3.14]
print(a)
print(b)
print(c)
print()

a, b, c = [1, 'a', 3.14]
print(a)
print(b)
print(c)
print()

(a, b) = (1, 2)
print(a)
print(b)
print()

a, b, c = 10, 20, 30
print(a)
print(b)
print(c)
print()

a, b, c = 10, {a, 2}, ['a', 'b']
print(a)
print(b)
print(c)
print()

a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)
c = id(b), id(a)
print(c)
print()

for e in 'XYZ':
    print(e)
print()
a, b, c = 'XYZ'
print(a)
print(b)
print(c)
print()

# Unpacking Sets:

s = {'p', 'y', 't', 'h', 'o', 'n'}
print(s)
for e in s:
    print(e)
print()

a, b, c, d, e, f = s
print()

# Unpacking Dictionaries:

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for num, (key, value) in enumerate(d.items(), start=1):
    print(f"{num}= {key}: {value}")
print()
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d, b, c, a = d
print(a)
print(b)
print(c)
print(d)
print()

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d, b, c, a = d.values()
print(a)
print(b)
print(c)
print(d)
print()

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d, b, c, a = d.items()
print(a)
print(b)
print(c)
print(d)
print()

