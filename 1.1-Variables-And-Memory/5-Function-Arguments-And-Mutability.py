""" Function Arguments and Mutability """


def process(s: str):
    print(f"Initial s # = {id(s)}")
    try:
        s += ' world!'
        print(s)
        print(f"Final s # = {id(s)}")
    except TypeError:
        print("The argument you're passing is not a valid parameter, please enter a string instead!")
    except Exception as e:
        print(e)
    finally:
        print("Thank you forever :)!!!")
    print()


my_var = "Hello"
process(my_var)
print(f"my_var # = {id(my_var)}")
print()


def modify_list(lst: list):
    print(f"Initial lst # = {id(lst)}")
    lst.append(100)
    print(f"Final lst # = {id(lst)}")


my_list = [1, 2, 3]
print(my_list)
print(id(my_list))
modify_list(my_list)
print(my_list)
print()


def modify_tuple(tpl: tuple):
    print(f"Initial tpl # = {id(tpl)}")
    tpl[0].append(100)
    print(f"Final tpl # = {id(tpl)}")
    print(tpl)


my_tuple = ([1, 2], 'a')
print(my_tuple)
modify_tuple(my_tuple)
print(my_tuple)
