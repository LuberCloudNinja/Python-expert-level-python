# i = 0
# while i < 5:
#     print(i)
#     i += 1
#
# print()
# print('***********************')
#
# i = 5
#
# while True:
#     print(i)
#     if i >= 5:
#         break
#
# print()
# print('***********************')
#
# min_lenght = 2
# name = input("Please enter your name: ")
#
# while not (len(name) >= min_lenght and name.isprintable() and name.isalpha()):
#     name = input("Please enter your name: ")
#
# print(f"Hello {name}")
#
# # The below code does the same as the one above:
#
# while True:
#     name = input("Please enter your name: ")
#     if len(name) >= min_lenght and name.isprintable() and name.isalpha():
#         break
# print(f"Hello {name}")
#
# print()
# print('***********************')
#
# a = 0
#
# while a < 10:
#     a += 1
#     if a % 2 == 0:
#         continue
#     print(a)
#
# print()
# print('***********************')
#
# l = [1, 2, 3]
# val = 10
# found = False
# idx = 0
#
# while idx < len(l):
#     if l[idx] == val:
#         found = True
#         break
#     idx += 1
# if not found:
#     l.append(val)
#
# print(l)
# print()
# # The below code does the same as the one above:
#
# l = [1, 2, 3]
# val = 10
# idx = 0
#
# while idx < len(l):
#     if l[idx] == val:
#         break
#     idx += 1
# else:
#     l.append(val)
#
# print(l)
#


# i = 0
#
# while i < 5:
#     print(i)
#     i += 1
#
# i = 5
#
# while True:
#     print(i)
#     if i >= 5:
#         break
# print()
# print("************")
#
# # +
#
# a = 0
#
# while a < 10:
#     a += 1
#     if a % 2 == 0:
#         continue
#     print(a)
# print()
# print("************")

# l = [1, 2, 3]
# val = 10
# found = False
# idx = 0
#
# while idx < len(l):
#     if l[idx] == val:
#         found = True
#         break
#     idx += 1
#
# if not found:
#     l.append(val)
#
# print(l)

# l = [1, 2, 3]
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
#
# print()
# print("************")
#
# a = 10
# b = 0
#
# try:
#     a // b
# except ZeroDivisionError:
#     print('division by 0')
# finally:
#     print('this always executes')
#
# print()
# print("************")

a = 0
b = 2

while a < 4:
    print('-----------------')
    a += 1
    b -= 1
    try:
        a / b
    except ZeroDivisionError:
        print(f'{a}, {b} division by 0')
        continue
    finally:
        print('this always executes')
    print(f'{a}, {b} - main loop')
   