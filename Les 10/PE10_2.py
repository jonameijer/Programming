b = 7
def verdubbelB():
    global b
    b = b+b
verdubbelB()
print(b)


import datetime
print('%H:%M:%S'.format(datetime.datetime.now))


def f(y):
    return 2*y+1
def g(x):
    return 5 + x + 10
print(f(3)+g(3))

