# using of enumarate

list_e = ["first", "second", "third", "fourth"]

# bad style
# for i in range(len(list_e)):
#     print(i, list_e[i])

# good style with enumerate
for number, element in enumerate(list_e):
    print(number, element)

# turn list to dict enumerated
new_dictionary = dict(enumerate(list_e))
print(new_dictionary)
