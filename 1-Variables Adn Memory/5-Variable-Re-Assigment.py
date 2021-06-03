#!/Users/luberlovemagic/opt/anaconda3/bin/python3

a = 10
print(hex(id(a)))
print(type(a))
print(id(a))
a = 15 # Here we're reassigning the value of 'a' to '15', this will move 'a' to a new address in the memory table.

print(hex(id(a)))
print(type(a))
print(id(a))