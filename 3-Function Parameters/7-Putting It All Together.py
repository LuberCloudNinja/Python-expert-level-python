#!/Users/luberlovemagic/opt/anaconda3/bin/python3

""" 1: """


def func1(a, b=2, *args, c=3, d):
    print(a, b, args, c, d)


func1(10, 20, 'x', 'y', 'z', c=4, d=1)
print('=========================')
func1(10, 20, 'x', 'y', 'z', d=1)
print('=========================')


def func2(a, b, *args, c=10, d=20, **kwargs):
    var_1 = (a, b, c, d)
    if args == () and kwargs == {}:
        for item1 in var_1:
            print(item1)
    elif args == ():
        for item2 in (var_1, kwargs):
            print(item2)
    elif kwargs == {}:
        for item3 in (var_1, args):
            print(item3)
    else:
        print(var_1, args, kwargs)


func2(1, 2, 2, 3, 4, 5, 6, e=20, f=40)
func1(10, 20, 'x', 'y', 'z', d=1)
func2(1, 2)
print('=========================')

""" 2: """


class Start:
    def __init__(self, a, b, *args, c: int = 10, d: int = 20, **kwargs):
        self._var_1 = (a, b, c, d)
        if args == () and kwargs == {}:
            for item1 in self._var_1:
                print(item1)
        elif args == ():
            for item2 in (*self._var_1, kwargs):
                print(item2)
        elif kwargs == {}:
            for item3 in (*self._var_1, args):
                print(item3)
        else:
            print(*self._var_1, args, kwargs)


Fred = Start(1, 2, 2, 3, 4, 5, 6, e=20, f=40)
# Leanita = Start(10, 20, 'x', 'y', 'z', d=1)
# Anna = Start(1, 2)
print('=========================')

""" 3: """


def cal_hi_lo_avg(*args, log_to_console: bool = False):
    hi = int(bool(args)) and max(args)
    lo = min(args) if len(args) > 0 else 0
    avg = (hi + lo) // 2
    if log_to_console:
        print(f"high={hi}, low={lo}, avg={avg}")
    return avg


is_debug = True
avg = cal_hi_lo_avg(1, 2, 3, 4, 5, log_to_console=is_debug)
print('=========================')
