# nested decorator in python


# so if we want to measure and do it n times
# we are going to wright one more function to wrap
def n_times(n):
    def inner(func):
        def wrapper(*args, **kwargs):
            rv = -1
            for _ in range(n):
                rv = func(*args, **kwargs)
                print("loop: ", rv)
            return rv
        return wrapper
    return inner


@n_times(3)
def add(x, y=10):
    return x + y


@n_times(2)
def sub(x, y=10):
    return x - y


print('add(10)',            add(10))
print('add(20, 30)',    add(20, 30))
# print('add("a","b")', add("a", "b"))
print('sub(10)',            sub(10))
print('sub(20, 30)',    sub(20, 30))
# print('sub("a","b")', sub("a", "b"))
