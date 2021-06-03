# i = 0
# while i < 5:
#     print(i)
#     i += 1
#
# print("****************")
#
# i = 5
#
# while True:
#     print(i)
#     if i >= 5:
#         break

# min_length = 2
# name = input("Please enter your name: ")
#
# while not len(name) >= min_length and name.isprintable() and name.isalpha():
#     name = input("Please enter your name: ")
#
# print(f"Hello {name}")


min_length = 2

# while True:
#     name = input("Please enter your name: ")
#     if len(name) >= min_length and name.isprintable() and name.isalpha():
#         break
# print(f"Hello {name}")
#
# print("****************")

# a = 0
# while a < 10:
#     a += 1
#     if a % 2 == 0:
#         continue
#     print(a)

# print("****************")

# l = [1, 2, 3, 10]
# val = 10
# idx = 0
# while idx < len(l):
#     if l[idx] == val:
#         break
#     idx += 1
# else:
#     l.append(val)
#
# print(l)

# print("****************")

# a = 10
# b = 1
#
# try:
#     a / b
# except ZeroDivisionError:
#     print("division by 0")
# finally:
#     print("this always executes")

# print("****************")

# a = 0
# b = 2
#
# while a < 4:
#     print("--------------")
#     a += 1
#     b -= 1
#
#     try:
#         a / b
#     except ZeroDivisionError:
#         print(f"{a} {b} - division by 0")
#         continue
#     finally:
#         print(f"{a} {b} - always executes")
#
#     print(f" {a} {b} - main loop")

# print("****************")


a = 0
b = 10

while a < 4:
    print("--------------")
    a += 1
    b -= 1

    try:
        a / b
    except ZeroDivisionError:
        print(f"{a} {b} - division by 0")
        break
    finally:
        print(f"{a} {b} - always executes")

    print(f" {a} {b} - main loop")
else:
    print("Code executed without a zero division error.")

