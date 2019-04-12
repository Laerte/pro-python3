from collections import OrderedDict


class OrderedMeta(type):

    @classmethod
    def __prepare__(mcs, name, bases):
        return OrderedDict()

    def __init__(cls, name, bases, attrs):
        print(attrs)


class Example(metaclass=OrderedMeta):
    b = 1
    a = 2
    c = 3
