import functools


def cachedproperty(name):
    def decorator(func):
        @property
        @functools.wraps(func)
        def wrapper(self):
            if name not in self.__dict__:
                self.__dict__[name] = func(self)
            return self.__dict__[name]
        return wrapper
    return decorator


class Example:
    @cachedproperty('attr')
    def attr(self):
        print('Getting value')
        return 42


example = Example()

print(example.attr)
print(example.attr)
