class Example:
    def method(self):
        pass


def dynamic(obj):
    return obj


Example.method = dynamic
print(Example.method)

ex = Example()
print(ex.method())


def dynamic():
    print('dynamic')


Example.method = dynamic
Example.method()
print(Example.method)
