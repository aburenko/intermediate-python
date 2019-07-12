# the difference is in [] and ()
# List comprehension
lc = [i for i in range(42)]
# Generator
g = (i for i in range(42))

# lc prints all stored elements
# and g is going to say that it is a generator object
print(lc)
print(g)

