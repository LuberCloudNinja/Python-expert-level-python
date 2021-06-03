#!/Users/luberlovemagic/opt/anaconda3/bin/python3

""" : Lambda and Sorting """

""" 1: """

help(sorted)

l = [1, 5, 4, 10, 9, 6]

print(sorted(l))
print("-------------------")
print("-------------------")
""" 2: """

l = ['c', 'B', 'D', 'a']

print(sorted(sorted(l)))
print("-------------------")
print(ord('a'))  # the "ord" function is use to order items inside it. Each one has a numeric value.
print("-------------------")
print(ord('A'))
print("-------------------")
sorted_items = sorted(l, key=lambda s: s.upper())
print(sorted_items)
print("-------------------")

""" 2: """

d = {'edf': 300, 'abc': 200, 'ghi': 100}
print(d)
print("-------------------")
results = [v for v in d.values()]
print(sorted(results))

# Another way to do but getting the keys base on the values sorted order:
d = {'edf': 300, 'abc': 200, 'ghi': 100}
for e in d:
    pass
print(sorted(d, key=lambda c: d[c]))
print("-------------------")
print("-------------------")


def dist_sq(x):
    return (x.real) ** 2 + (x.imag) ** 2


print(dist_sq(1 + 1j))
print("-------------------")

l = [3 + 3j, 1 - 1j, 0, 3 + 0j]
print(sorted(l, key=dist_sq))
# or

print(sorted(l, key= lambda x: (x.real) ** 2 + (x.imag) ** 2))
print("-------------------")
print("-------------------")

l = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']
print(sorted(l))
# Return ordered value using the last character in each item on the "l" list:
print((sorted(l, key=lambda s: s[-1])))


