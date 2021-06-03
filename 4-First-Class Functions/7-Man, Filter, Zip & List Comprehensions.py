#!/Users/luberlovemagic/opt/anaconda3/bin/python3

""" Map, Filer, Zip & List Comprehensions """

""" 1.1: Map """


def fact(n):
    return 1 if n < 2 else n * fact(n - 1)


print(fact(3))
print("-------------------")
print(fact(4))
print("-------------------")
results = list(map(fact, range(6)))
print(results)
print("-------------------")

""" 1.2: """

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]
l3 = [100, 200, 300, 400]

results = list(map(lambda x, y, z: x + y + z, l1, l2, l3))
print(results)
print("-------------------")

# """ 1.3: """
# results = filter(map(lambda x, y: x + y, l1, l2, l3))
# print(results)
# print("-------------------")

""" 2.1 Filer Function: """

x = range(25)
print(x)
for i in x:
    print(i)
print("-------------------")
print(list(filter(lambda x: x % 3 == 0, range(25))))
print("-------------------")
print(list(filter(None, [1, 0, 4, 'a', '', None, True, False])))
print("-------------------")
print("-------------------")

""" 3.1: Zip Function: """

l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]
l3 = "python"

results = zip(l1, l2, l3)
for x in results:
    print(x)
print("-------------------")

# or: To repeat this as often as we want we'll need to convert it into a list:

results = list(zip(l1, l2, l3))
print(results)
print("-------------------")

""" 3.2: """
print(list(zip(range(10000), "python")))
print("-------------------")
print("-------------------")

""" 1.1 List Comprehensions: """

l = range(10)
print(list(l))
print("-------------------")
print(list(map(fact, l)))
print("-------------------")
# Now with List Comprehensions:
results = [fact(n) for n in range(10)]
print(results)
print("-------------------")
# Now the same results but with generator expression:
results = (fact(n) for n in range(10))
for x in results:
    print(x)
print("-------------------")
# or: To reuse it as often as need it we;ll need too make it into a list:
results = list(fact(n) for n in range(10))
print(results)
print("-------------------")

""" 1.1 """
l1 = [1, 2, 3, 4, 5, 6]
l2 = [10, 20, 30, 40]
l3 = [100, 200, 300, 400]

# Using a map function:
print(list(map(lambda x, y: x + y, l1, l2)))
print("-------------------")
# Using a list comprehension:
results = [x + y for x, y in zip(l1, l2)]
print(results)
# Lets us filter the about but with a filter function first:
print("-------------------")
print(list(filter(lambda x: x % 2 == 0, map(lambda x, y: x + y, l1, l2))))
print("-------------------")
# Lets filter now with a list comprehension:
results = [x + y for x, y in zip(l1, l2) if (x + y) % 2 == 0]
print(results)
print("-------------------")


