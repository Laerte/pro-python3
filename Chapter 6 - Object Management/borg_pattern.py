class Base:
    def __init__(self):
        print('Base')

class Borg:
    _namespace = {}
    def __new__(cls, *args, **kwargs):
        print('Borg')
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._namespace.setdefault(cls, {})
        return obj

class TestOne(Borg):
    pass

class TestTwo(Borg):
    pass


a = TestOne()
b = TestOne()
c = TestTwo()

print(hasattr(a, 'spam'))

b.spam = 'eggs'

print(hasattr(a, 'spam'))
print(a.spam)

print(Borg._namespace)

# print(c.spam)

d = TestTwo()
d.spam = 'burguer'

print(c.spam)

print(a.spam)
