#!/Users/luberlovemagic/opt/anaconda3/bin/python3

""" 1: """
a = 10
b = 10

print(id(a))
print(id(b))

print("a is b", a is b)
print("a == b", a == b)

""" 2: """

a = 500
b = 500
print(id(a))
print(id(b))

print("a is b", a is b)
print("a == b", a == b)

""" 3: """

a = [1,2,3]
b = [1,2,3]
print(id(a))
print(id(b))
print("a is b", a is b)
print("a == b", a == b)

""" 4: """

a = 10
b = 10.0
print(id(a))
print(id(b))
print("a is b", a is b)
print("a == b", a == b)

""" 5: """

a = 10 + 0j
b = 10.0
print(type(a))
print(type(b))

print("a is b", a is b)
print("a == b", a == b)

""" 6: """

print(id(None))
print(type(None))

a = None
b = None
c = None

print(a is b and a is c)

