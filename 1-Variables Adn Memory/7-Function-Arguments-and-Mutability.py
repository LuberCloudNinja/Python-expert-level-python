#!/Users/luberlovemagic/opt/anaconda3/bin/python3

""" 1: Mutability Using Strings """


def process(s):
    print(f'Initial s # = {id(s)}')
    s = s + ' world'
    print(f'Final s # = {id(s)}')


my_var = 'hello'
print(f'my_var # {id(my_var)}')
process(my_var)

""" 2: Mutability Using List"""


def modify_list(lst):
    print(f'Initial s # = {id(lst)}')
    lst.append(100)
    print(f'Final s # = {id(lst)}')


my_list = [1, 2, 3]
print(id(my_list))
modify_list(my_list)

""" 3: Mutability Using Tuple """


def modify_tuple(t):
    print(f'Initial s # = {id(t)}')
    t[0].append(100)
    print(f'Final s # = {id(t)}')
    print(t)


my_tuple = ([1, 2], 'a')
print(my_tuple)
print(id(my_tuple))
modify_tuple(my_tuple)
print(my_tuple)
