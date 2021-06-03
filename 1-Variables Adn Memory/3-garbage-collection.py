#!/Users/luberlovemagic/opt/anaconda3/bin/python3

import ctypes, gc


def ref_count(address):
    """ This function will give us the exact value of counts in the memory table"""
    return ctypes.c_long.from_address(address).value


def object_bt_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Object Not Found"


class A:
    def __init__(self):
        """ This construct will printout the memory address of the instance of class 'A' and 'B' """
        self.b = B(self)
        print('A: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))  # The professor did it this way.
        print(f"A: self: {hex(id(self))}, b: {hex(id(self.b))}")  # My way


class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))  # The professor did it this way.
        print(f"B: self: {hex(id(self))}, a: {hex(id(self.a))}")  # My way


gc.disable()  # Disabling the default garbage collector.

my_var = A()
print(hex(id(my_var)))
print(hex(id(my_var.b)))
print(hex(id(my_var.b.a)))

a_id = id(my_var)
b_id = id(my_var.b)
print(hex(a_id))
print(hex(b_id))

print(ref_count(a_id))  # This will give us the count of object in the memory table.
print(ref_count(b_id))

print(object_bt_id(a_id))
print(object_bt_id(b_id))

my_var = None  # This will destroy the variable and the count for the below object and it should come down to 1
# because each reference each other.

print(ref_count(a_id))
print(ref_count(b_id))

print(object_bt_id(a_id))
print(object_bt_id(b_id))

# Run garbage collector manually because we disable it previously.

gc.collect()
"""Below we should get the "Object Not Found" return value from the function because...
we manually ran the garbage collector command above and therefore is no longer in memory. """
print(object_bt_id(a_id))
print(object_bt_id(b_id))

""" And again, because we manually ran the garbage collector function the count now should be 0 in for each object."""
print(ref_count(a_id))
print(ref_count(b_id))



