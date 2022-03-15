import sys
import ctypes

a = [1, 2, 3]
print(id(a))

print(sys.getrefcount(a))


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


print(ref_count(id(a)))
print()
b = a
print(id(b))
print(ref_count(id(a)))
c = 10
print(id(c))
print(ref_count(id(a)))
b = None
print(id(b))
print(ref_count(id(a)))

a_id = id(a)
a = None
print(ref_count(id(a_id)))


