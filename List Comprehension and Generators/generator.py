input_list = [42, 33, 5, 25, 55, 1, 0, 63, 100]


def div_by_2(number):
    # can be tricky :)
    if number & 0x01 == 0x00:
        return True
    else:
        return False


# create generator over the list
div_by_2_generator = (i for i in input_list if div_by_2(i))
# on this example we see that the pointer of the generator is not changing its position
# after using or with the new foreach using
# to print all elements
for i in div_by_2_generator:
    print(i)
    if i == 0:
        print("exit")
        break
# or
[print(i) for i in div_by_2_generator]

# reset the pointer of that generator
div_by_2_generator = (i for i in input_list if div_by_2(i))
# convert to list
div_by_2_list = [i for i in div_by_2_generator]
print(div_by_2_list)

