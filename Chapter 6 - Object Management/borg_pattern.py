class Base:
    def __init__(self):
        print('Base')

class Borg:
    _namespace = {}
    def __new__(cls, *args, **kwargs):
        print('Borg')
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._namespace
        return obj

class Testing(Base, Borg):
    pass


a = Testing()
b = Testing()

print(hasattr(a, 'attribute'))

b.attribute = 'value'

print(hasattr(a, 'attribute'))
print(a.attribute)

print(Borg._namespace)
