#!/Users/luberlovemagic/opt/anaconda3/bin/python3

""" 1: """
a = "hello"
b = a
print(hex(id(a)))
print(hex(id(b)))

""" 2: """

a = "hello"
b = "hello"

print(hex(id(a)))
print(hex(id(b)))

b = "hello world"  # Now the ID of b in memory will change
print(hex(id(b)))

""" 3: """
a = [1,2,3]
b = a
print(hex(id(a)))
print(hex(id(b)))
b.append(100)
print(a)
print(b)
print(hex(id(a)))
print(hex(id(b)))


""" 4: """
a = 10
b = 10
print(hex(id(a)))
print(hex(id(b)))
