#!/Users/luberlovemagic/opt/anaconda3/bin/python3

""" 1: List """

my_list = [1, 2, 3]
print(type(my_list))
print(id(my_list))
my_list.append(4)  # Appending an object inside the list won't modify the ID in the memory table.
print(my_list)
print(id(my_list))
my_list_1 = [1, 2, 3]
print(id(my_list_1))
my_list_1 = my_list_1 + [4]  # Concatenating will create a new object in memory therefore the id of "my_list_1" will
# changed.
print(my_list_1)
print(id(my_list_1))

""" 2: Dictionaries """
my_dict = dict(key1=1, key2='a')
print(my_dict)
print(id(my_dict))
my_dict['key3'] = 10.5
print(my_dict)
print(id(my_dict))

""" 3: Tuples """

t = (1, 2, 3)
print(id(t))
print(id(t[0]))  # This will provide us with the ID in memory of the first item in the tuple.
print(id(t[1]))  # This will provide us with the ID in memory  of the second item in the tuple.
t = ([1,2,], [3,4])
print(t)
print(id(t))
print(t[0])
print(t[1])

t[0].append(3) # Even though a tuple is immutable we can make mutable operations inside because it contains a list.
# We just need to reach out to the list inside the tuple to make the adjustment in the elements.
print(t)
print(id(t))



