#!/Users/luberlovemagic/opt/anaconda3/bin/python3

""" We just want to show how a single variable changed object types"""
a = "hello"
print(type(a))
a= 10
print(type(a))

a = lambda x: x**2

print(a(2))

print(type(a))

a = 3 + 4j

print(type(a))