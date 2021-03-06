import ctypes
import gc


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


def object_by_id(object_id: int):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exist"
    return "Not Found"


class A:
    def __init__(self):
        self.b = B(self)
        print(f'A: self:{hex(id(self))}, b:{hex(id(self.b))}')


class B:
    def __init__(self, a):
        self.a = a
        print(f'B:self:{hex(id(self))}, a:{hex(id(self.a))}')


gc.disable()
my_var = A()
print(my_var)
print()
print(hex(id(my_var)))
print(my_var.b)
print()
print(hex(id(my_var.b)))
print(hex(id(my_var.b.a)))
print()
a_id = id(my_var)
b_id = id(my_var.b)
print(hex(a_id))
print(hex(b_id))
print()
print(ref_count(a_id))
print(ref_count(b_id))
print()
print(object_by_id(a_id))
print(object_by_id(b_id))
my_var = None
print()
print(ref_count(a_id))
print(ref_count(b_id))
print()
print(object_by_id(a_id))
print(object_by_id(b_id))
gc.collect()
print(object_by_id(a_id))
print(object_by_id(b_id))
print()
print(ref_count(a_id))
print(ref_count(b_id))
