import weakref


class Example:
    pass


e = Example()
print(e)

ref = weakref.ref(e)
print(ref)
print(ref())

del e
print(ref)
print(ref())

ref = weakref.ref(Example())
print(ref)
print(ref())


def example():
    e = Example()
    ref = weakref.ref(e)
    return ref


e = example()
print(e)
print(e())
