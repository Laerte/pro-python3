class A:
    pass


class B(A):
    pass


print(issubclass(B, A))
print(issubclass(B, B))

print(B.__bases__)
print(A.__subclasses__())
print(B.__mro__)

try:
    import custom_library
except ImportError:
    custom_library = None


class Custom:
    has_library = custom_library is not None


print(Custom.has_library)

# Creating Classes at Runtime


class Example(int):
    spam = 'eggs'


print(Example)

Example = type('Example', (int,), {'spam': 'ovos'})

print(Example)
