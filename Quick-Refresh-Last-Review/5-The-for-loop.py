i = 0

for i in range(5):
    print(i)

print()
print("************")

for i in [1, 2, 3, 4]:
    print(i)

print()
print("************")

for c in 'hello':
    print(c)

print()
print("************")

for x in ('a', 'b', 'c', 4):
    print(x)

print()
print("************")

for x in [(1, 2,), (3, 4,), (5, 6,)]:
    for i in x:
        print(i)

print()
print("************")

for i, j in [(1, 2,), (3, 4,), (5, 6,)]:
    print(i, j)

print()
print("************")

for i in range(5):
    if i == 3:
        continue
    print(i)

print()
print("************")

for i in range(1, 10):
    print(i)
    if i % 7 == 0:
        print('Multiple of 7 found.')
        break
else:
    print('No multiples of 7 in the range.')

print()
print("************")

for i in range(5):
    print('--------------------')
    try:
        10 / (i - 3)
    except ZeroDivisionError:
        print('Divided by 0')
        break
    finally:
        print(f"Always run {i}!")
    print(i)

print()
print("************")

s = 'hello'
i = 0
for c in s:
    print(i, c)
    i += 1

print()
print("************")

s = 'hello'

for i in range(len(s)):
    print(i, s[i])

print()
print("************")

for i, c in enumerate(s):
    print(i, c)
   