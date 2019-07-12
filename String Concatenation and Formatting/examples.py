# join and split
myString = ["string", "split", "example"]
# bad style
newString = ""
for string in myString:
    newString += string
    newString += " "
print(newString)
# good style
print(" ".join(myString))

# + and format
hh = 12
mm = 30
# bad style
print("Time is " + str(hh) + ":" + str(mm))
# good style
print("Time is {}:{}".format(hh, mm))
