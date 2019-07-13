# library side
# cant be changed from user side


class BaseMeta(type):
    def __new__(cls, name, bases, body):
        # print('BaseMeta.__new__ cls:{} name:{} bases:{} body:{}'
        #       .format(cls, name, bases, body))
        if name is not 'Base' and 'bar' not in body:
            raise TypeError("bad user class")
        return super().__new__(cls, name, bases, body)


class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar

    def __init_subclass__(cls, *a, **kw):
        print("init subclass", a, kw)
        return super().__init_subclass__(*a, **kw)
