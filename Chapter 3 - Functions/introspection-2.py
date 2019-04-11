import inspect
# Identifying Object Types


def example():
    pass


print(example.__name__)

example = lambda: 'test'

print(example.__name__)

print(type('example'))


class Test:
    pass


print(type(Test))
print(type(Test()))


def test(value):
    if isinstance(value, int):
        print('Found a integer!')


print(test('0'))
test(0)


# Modules and Packages

print(example.__module__)

# Docstrings


def example():
    """This is just an example to illustrate docstring access."""
    pass


print(example.__doc__)  # output docstring


def divide(x, y):
    """
    divide(integer, integer) -> floating point

    This is a more complex example, with more comprehensive documentation.
    """
    return float(x) / y  # Use float() for compatibility prior to 3.0


print(divide.__doc__)

print(inspect.getdoc(divide))


def clone(obj, count=1):
    """
    clone(obj, count=1) -> list of cloned objects

    Clone an object a specified number of times, returning the cloned
    objects as a list. This is just a shallow copy only.

    obj
        Any Python object
    count
        Number of times the object will be cloned

    >>> clone(object(), 2)
    [<object object at 0x12345678>, <object object at 0x87654321>]s
    """
    import copy
    return [copy.copy(obj) for x in count]


print(inspect.getdoc(clone))
