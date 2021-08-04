#!/Users/luberlovemagic/opt/anaconda3/bin/python3

""" Examples: """
""" 1: List """

l = list(range(1, 7))
# 1

a = l[0]
b = l[1:]
print(a)
print(b)

# 2
a, b = l[0], l[1:]
print(a)
print(b)

# 3
a, *b = l
print(a)
print(b)

# 4

s = 'python'
a, *b = s

# 5

[a, b, c] = 'XYZ'
print(a)
print(b)
print(c)
print('=================')

[a, *b] = 'XYZ'
print(a)
print(b)
print('=================')

a, b, *c = 'python'
print(a)
print(b)
print(c)
print('=================')

a, b, *c, d = 'python'
print(a)
print(b)
print(c)
print(d)
print('=================')

# 6

s = 'python'
a, b, c, d = s[0], s[1], s[2:-1], s[-1]
*c, = c  # this will pack the elements in object c inside a list.
print(a)
print(b)
print(c)
print(d)
print('=================')

# 7:

l1 = [1, 2, 3]
l2 = [4, 5, 6]
*l, = *l1, *l2
# or:
ll = [*l1, *l2]
print(l)
print(ll)
print('=================')
# 7:

l1 = [1, 2, 3]
s = 'abc'
i = [*l1, *s]
# or:
*m, = *l1, *s
print(i)
print(m)
print('=================')

# 8:
l1 = [1, 2, 3]
s1 = {'x', 'y', 'z'}  # Remember that sets cant guarantee the order of the elements:
*s, = *l1, *s1
# or
m = [*l1, *s1]
print(s)
print(m)

print('=================')

# 9 =

s1 = 'abc'
s2 = 'cde'
print([*s1, *s2])
print({*s1, *s2})

s = {10, -99, 3, 'd'}

for c in s:
    print(c)
print('=================')
a, b, c, d = s
print(a, b, c, d)
print('=================')
a, b, *c = s
print(a, b, c)
# 10:

*c, = s
print(c)

# 10:

# s1 = set(range(1, 4))
# s2 = set(range(3, 6))
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s = [*s1, *s2]
# or:
*m, = *s1, *s2
print(s)
print(m)
print('=================')

s1 = {1, 2, 3}
s2 = {3, 4, 5}
x = {*s1, *s2}
print(x)
# print(help(set))
print('=================')
print(s1.union(s2))
print('=================')
# 11:

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
s4 = {7, 8, 9}

s5 = s1.union(s2, s3, s4)

s6 = {*s1, *s2, *s3, *s4}
print(s6)
print('=================')
# Or to keep all the elements in the four sets we can unpack them.
s7 = [*s1, *s2, *s3, *s4]
print(s7)
print('=================')

# 12:

# Dictionaries:

d1 = {'key1': 1, 'key2': 2}
d2 = {'key2': 3, 'key4': 4}
d7 = {**d1, **d2}
print(d7)
print('=================')

# 13:
# 1 Nested unpacking:

a, *b, e = [1, 2, 3, 'XY']
print(a)
print(b)
print(e)
print('=================')

a, b, (c, d) = [1, 2, 'XY']
print(a)
print(b)
print(c)
print(d)
print('=================')

a, b, (c, d, *e) = [1, 2, 'python']
print(a)
print(b)
print(c)
print(d)
print(e)
print('=================')

# Same results using slicing:

l = [1, 2, 3, 4, 'python']
a, *b, (c, d, *e) = l
print(a)
print(b)
print(c)
print(d)
print(e)
print('=================')
# Another way using slicing:

print(l[0])
print(l[1:4])
print(l[-1][0:2])
print(list(l[-1][2:]))
print('=================')

# Another way using slicing:
a, b, c, d = l[0], l[1:4], l[-1][0:2], list(l[-1][2:])
print(a, b, c, d)

print('=================')

print(l[0])
print(l[1:4])
print(list(l[-1]))
