#!/Users/luberlovemagic/opt/anaconda3/bin/python3
import sys
import ctypes

a = [1, 2, 3]

print(id(a))
print(sys.getrefcount(a))  # This will show us the exact count in memory in the variable.
# print(hex(a))
print(hex(id((a))))


def ref_count(address: int):
    "This function will allow us to get the count in memory but without adding and extra value."
    return ctypes.c_long.from_address(address).value


b = a
print(id(b))
c = a
print(id(a))

print(ref_count(id(a)))