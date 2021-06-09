# i = 0
#
# while i < 5:
#     print(i)
#     i += 1
# i = None
#

for i in range(5):
    print(i)

print("*******************")

for i in [1, 2, 3, 4]:
    print(i)

print("*******************")

for c in "hello":
    print(c)

print("*******************")

for x in ('a', 'b', 'c', 4):
    print(x)

print("*******************")

for x in [(1, 2), (3, 4), (5, 6)]:
    print(*x)

print("*******************")

for i in range(5):
    if i == 3:
        continue
    print(i)

print("*******************")

for i in range(5):
    if i == 3:
        break
    print(i)

print("*******************")

for i in range(1, 5):
    print(i)
    if i % 7 == 0:
        print("Multiple of 7 found")
        break
else:
    print("No multiples of 7s in the range")

print("*******************")

for i in range(5):
    print("-----------------------")
    try:
        10 / (i - 3)
    except ZeroDivisionError:
        print("Divided by 0")
        continue
    finally:
        print("Always run")
    print(i)

print("*******************")
s = "hello"
for i in range(len(s)):
    print(i, s[i])
print("*******************")

e = "hello"
for e, num in enumerate(e):
    print(f"{e} {num}")
