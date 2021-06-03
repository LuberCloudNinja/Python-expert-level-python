#!/Users/luberlovemagic/opt/anaconda3/bin/python3

from datetime import datetime
import time

""" 1: """
# We can see how time keep changing every time we print the datetime.utcnow object.
print(datetime.utcnow())
print(datetime.utcnow())
print(datetime.utcnow())
print('========================')
print('========================')

""" 2: """


def log1(msg, *, dt: str = datetime.utcnow()):
    print(f"Time-{dt}, With-{msg.title()}")


log1('message 1', dt='2010-01-01 00:00:00')
print('========================')
log1('message 2')
log1('message 3')
print('========================')
print('========================')
""" 3: """


def log3(msg, *, dt=None):
    if not dt:
        dt = dt or datetime.utcnow()
    """If we don't pass an argument when calling the function in dt, then we will add 
datetime.utcnow object as dt, this solve the above function issue,
when calling the function passing 'dt' as an argument and time not changing"""
    print(f"Time-{dt}, With-{msg.title()}")


log3('message 1', dt='2010-01-01 00:00:00')
print('========================')
log3('message 2')
time.sleep(3)
log3('message 3')
print('========================')
print('========================')

""" 4: Another way to do it below: """


def log4(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    print(f"Time-{dt}, With-{msg.title()}")


log4('message 1', dt='2010-01-01 00:00:00')
print('========================')
log4('message 2')
time.sleep(3)
log4('message 3')
print('========================')
print('========================')

""" 5: """

