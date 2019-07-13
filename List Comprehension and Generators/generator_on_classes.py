# based on PyData Seattle 2017
from time import sleep


def compute():
    for i in range(10):
        sleep(.5)
        yield i


# for x in compute():
#     print(x)


# this way is that e.g. good style to give
# the suquence for an api

class VeryImportantClass:
    def __first_to_call(self):
        print("first")

    def __second_to_call(self):
        print("second")

    def __third_to_call(self):
        print("third")

    def api(self):
        self.__first_to_call()
        yield
        self.__second_to_call()
        yield
        self.__third_to_call()


vip = VeryImportantClass()
for x in vip.api():
    pass
