# initial variables
a = ["zip", "is", "not", "an", "archive"]
b = [34, 44, 19, 88, 43]
c = ['c', 'a', '+', '@']

# zip is a function for combining or uncombining of values
# to a list/dict or out of list/dict

# so combine a and b in one list with zip is:
print(list(zip(a, b)))
# a, b and c
print(list(zip(a, b, c)))

# try to combine a and c with different length
# this causes to take the length of smallest list
print(list(zip(a, c)))

# with two argument dict can be created
print(dict(zip(b, c)))


# uncombined
print("uncombine")
zipped_list = zip(a, b)
unzipped_a, unzipped_b = zip(*zipped_list)
print(unzipped_a)
print(unzipped_b)