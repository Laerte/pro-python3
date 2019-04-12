import random


# Creating Instances
class Example:
    def __init__(self):
        self.initialized = True


e = Example()
print(e.initialized)


class Example2:

    def __init__(self, name, value='"'):
        self.name = name
        self.value = value


e = Example2('testing')
print(e.name)
print(e.value)


# Automatic Subclasses
class Example:
    def __new__(cls, *args, **kwargs):
        cls = random.choice(cls.__subclasses__())
        return super(Example, cls).__new__(cls, *args, **kwargs)


class Spam(Example):
    pass


class Eggs(Example):
    pass


for x in range(5):
    print(Example())

# Dealing with Attributes


class AttributeDict(dict):
    author = 'Laerte'

    def __getattr__(self, name):  # only gets called for attributes that don’t actually exist, try use:
        # __getattribute__ if you need to catch every attribute regardless
        try:
            self[name]
        except Exception:  # RAISE THE RIGHT EXCEPTION
            raise AttributeError('AttributeError: {}'.format(name))

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        del self[name]


d = AttributeDict(spam='eggs')
print(d['spam'])
print(d.spam)
print(d.author)
d.spam = 'ham'
print(d.spam)
del d.spam

try:
    print(d.spam)
except Exception as e:
    print(e)


# String Representations
class Book:
    def __init__(self, title, author=None):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title

    def __repr__(self):
        return '<%s by %s>' % (self.title, self.author or '<UnknownAuthor>')


print(Book('Pro Python'))
