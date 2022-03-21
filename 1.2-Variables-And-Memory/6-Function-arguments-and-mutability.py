def process(s: str):
    print(f"Initial s # = {id(s)}")
    s = s + " World!"
    print(f"Final s # = {id(s)}")


my_var = "hello"

print(f"my_var # = {id(my_var)}")
process(my_var)
print()
print("*******************")


def modify_list(lst):
    print(f"Initial lst # = {id(lst)}")
    lst.append(100)
    print(f"Final lst # = {id(lst)}")


my_list = [1, 2, 3]
print(id(my_list))
modify_list(my_list)
print(my_list)
print()
print("*******************")

def modify_tuple(t):
    print(f"Initial lst # = {id(t)}")
    t[0].append(100)
    print(f"Final lst # = {id(t)}")


my_tuple = ([1, 2], 'a')
print(id(my_tuple))
modify_tuple(my_tuple)
print()
print("*******************")