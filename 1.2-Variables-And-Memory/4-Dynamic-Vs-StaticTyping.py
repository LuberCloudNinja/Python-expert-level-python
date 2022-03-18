a = "hello"
print(type(a))
a = 10
print(type(a))
a = lambda x: x ** 2
print(a(5))
print(type(a))
print("****************************")
print()
""" Variable Re-Assignment"""

a = 10
print(hex(id(a)))
print(type(a))
a = 15
print(hex(id(a)))
a = a + 1
print(hex(id(a)))
a = 10
b = 10
print(hex(id(a)))
print(hex(id(b)))