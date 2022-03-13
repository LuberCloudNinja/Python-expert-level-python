a = 6

if a < 5:
    print('a < 5')
else:
    print('a >= 5')

print()
print('***********************')

a = 10
if a < 5:
    print('a < 5')
else:
    if a < 10:
        print('5 <= a < 10')
    else:
        print('a >= 10')

print()
print('***********************')

a = 10

if a < 5:
    print('a < 5')
elif a < 10:
    print('5 <= a < 10')
else:
    print('a >= 10')

print()
print('***********************')

a = 25

if a < 5:
    b = 'a < 5'
else:
    b = 'a >= 5'

print(b)

# Another way to do the above:
b = 'a < 5' if a < 5 else 'a >= 5'
print(b)
