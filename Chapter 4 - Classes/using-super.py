class A(object):
    def afunction(self):
        print('afunction from Class A')


class B(A):
    def __init__(self):
        print('B is constructed!!!')  # constructor for B

    def afunction(self):
        return super(B, self).afunction()


sample1 = B()
sample1.afunction()


class NoneDictionary(dict):
    def __getitem__(self, name):
        try:
            return super(NoneDictionary, self).__getitem__(name)
        except KeyError:
            return None


d = NoneDictionary()
print(d['example'])
d['example'] = True
print(d['example'])


class A():
    def test(self):
        return 'A'


class B(A):
    def test(self):
        return 'B->' + super(B, self).test()


print(B().test())


class C(A):
    def test(self):
        return 'C'


class D(B, C):
    pass


print(D().test())


class B(A):
    def test(self):
        return 'B->' + super(C, self).test()


class D(B, C):
    pass


print(D().test())

try:
    print(B().test())
except TypeError as e:
    print(str(e))
