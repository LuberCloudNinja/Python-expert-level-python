#!/Users/luberlovemagic/opt/anaconda3/bin/python3

""" 1: Function that add grocery items into a list """


def add_item1(name, quantity, unit, grocery_list):
    grocery_list.append(f"{name} ({quantity} {unit})")
    return grocery_list


store1 = []
store2 = []

print(add_item1('banana', 2, 'units', store1))
print(add_item1('milk', 1, 'liter', store1))
print(store1)
print('========================')
print(add_item1('python', 1, 'medium-rare', store2))
print(store2)
print('========================')
print('========================')

""" 2: In this example if the user don't provide us with a grocery list we'll create a new one in the function """


def add_item2(name, quantity: int, unit, grocery_list: list = []):
    grocery_list.append(f"{name} ({quantity} {unit})")
    return grocery_list


store3 = add_item2('banana', 2, 'units')
store4 = add_item2('milk', 1, 'liter')
print(store3)

print('========================')
print('========================')


def add_item3(name, quantity: int, unit: str or int = 1, grocery_list: list = None):
    if not grocery_list:
        grocery_list = []
    grocery_list.append(f"{name} ({quantity} {unit})")
    return grocery_list


store5 = []
store4 = add_item3('banana', 2, 'units')
print(add_item3('milk', 1, 'liter', store5))
print('========================')
print('========================')

""" 3: Factorial function: """


def factorial1(n):
    if n < 1:
        return 1
    else:
        print(F"calculating {n}!")
        return n * factorial1(n - 1)


factorial1(2)

""" 4: Factorial function: """


def factorial2(n, *, cache):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print(F"calculating {n}!")
        result = n * factorial2(n - 1, cache=cache)
        cache[n] = result
        return result


cache = {}
print(factorial2(3, cache=cache))
print(cache)
print(factorial2(3, cache=cache))
print('========================')
print('========================')

""" 5: Another way to do it is: """


def factorial3(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print(F"calculating {n}!")
        result = n * factorial3(n - 1)
        cache[n] = result
        return result


print(factorial3(3))
print(factorial3(4))