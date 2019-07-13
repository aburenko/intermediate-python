# decorator in python
# got two functions add and sub that are trivial
# we want to count elapsed time for this functions
# in order to not rewrite the functions we can use the decorators
from time import time


# this is our decorator function that count time
def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        # do some math
        x = [5+7 for i in range(500000)]
        after = time()
        print('elapsed time', after - before)
        return rv
    return f

# the actual way how decorator works is:
#
# def add(x, y=10):
#     return x + y
# add = timer(add)
#
# so it reinitialize the function with a new one
# and adds a new functionality to it
# but we can wright it as @timer as follows


@timer
def add(x, y=10):
    return x + y


@timer
def sub(x, y=10):
    return x - y


print('add(10)',            add(10))
print('add(20, 30)',    add(20, 30))
# print('add("a","b")', add("a", "b"))
print('sub(10)',            sub(10))
print('sub(20, 30)',    sub(20, 30))
# print('sub("a","b")', sub("a", "b"))

exit(0) # prevent getting to explanation code

# a function in python has following properties
# e.g.:
# shows where the function is stored
print(add)
# __name__
print(add.__name__)
# __module__ shows to what module is func related
print(add.__module__)
# __defaults__ default argument
print(add.__defaults__)
# __code__.co_code show binary code
print(add.__code__.co_code)