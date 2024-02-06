# args is a tuple with as many arguments as the caller provided
def add(*args):
    r = 0
    for n in args:
        r += n
    return r

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

