""" Callables """

print(callable(print))

print("hello")
result = print("hello")
print(result)
l = [1, 2, 3]
callable(l.append)
result1 = l.append(4)
print(l)


