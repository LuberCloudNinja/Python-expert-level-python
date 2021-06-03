#!/Users/luberlovemagic/opt/anaconda3/bin/python3

"""1: """
# This is the range [-5, 256] that will be used by the memory catch to keep different memory reference (variables
# with the same value) in the same memory table and ID.


a = 10
b = 10
print(id(a))
print(id(b))

a = -5
b = -5

print(id(a), id(b))
print(a is b)

a = 256
b = 256
print(id(a), id(b))
print(a is b)

# Here the memory id of 'a' and 'b' should be different because is not in the catch range of -5 to 256.
a = 257
b = 257

print(id(a), id(b))
print(a is b)

a = 10
b = int(10)
c = int('10')
d = int('1010', 2)

print(id(a), id(b), id(c), id(d))
print(a is b is c is d)
print(a,b,c,d)
print(bin(int('1010', 2)))
print(0b1010)

