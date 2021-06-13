""" Object Mutability """


def object_mutability_1():
    my_list = [1, 2, 3]
    print(id(my_list))
    print(type(my_list))
    my_list.append(4)
    print(my_list)
    print(id(my_list))


def object_mutability_2():
    my_list_1 = [1, 2, 3]
    print(id(my_list_1))
    my_list_1 = my_list_1 + [4]
    print(id(my_list_1))
    print(my_list_1)


def object_mutability_3():
    my_dict = {'key1': 1, 'key2': 'a'}
    print(my_dict)
    print(id(my_dict))
    my_dict['key3'] = 10.5
    print(my_dict)


def object_mutability_4():
    t = (1, 2, 3)
    print(id(t))
    print(t[0])
    print(id(t[0]))
    print(id(t[1]))


def object_mutability_5():
    t = ([1, 2], [3, 4])
    print(id(t))
    print(t[0][1])
    t[0].append(3)
    print(t)


object_mutability_1()
print()
object_mutability_2()
print()
object_mutability_3()
print()
object_mutability_4()
print()
object_mutability_5()
