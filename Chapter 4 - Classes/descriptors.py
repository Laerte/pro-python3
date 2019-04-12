import datetime
import time


class CurrentTime:
    def __get__(self, instance, owner):
        return datetime.datetime.now()


class Example:
    time = CurrentTime()


print(Example().time)

#time.sleep(30)  # Wait 30 seconds
#print(Example().time)


class LoggedAttribute:
    def __init__(self):
        self.log = []
        self.value_map = {}

    def __set__(self, instance, value):
        self.value_map[instance] = value
        log_value = (datetime.datetime.now(), instance, value)
        self.log.append(log_value)

    def __get__(self, instance, owner):
        if not instance:
            return self  # This way, the log is accessible

        return self.value_map.get(instance, None)


class Example:
    value = LoggedAttribute()


e = Example()
e.value = 'testing'
print(e.value)
print(Example.value.log)


class Example:
    def method(self):
        return 'done!'


print(type(Example.method))
print(Example.method)

ex = Example()
print(type(ex.method))

# self gets passed automatically now
print(ex.method())

# And the underlying function is still the same
print(Example.method is ex.method.__func__)


class Example:
    @classmethod
    def method(cls):
        return cls


print(Example.method())
print(Example.method)


class ExampleMeta(type):
    def method(cls):
        return cls


class Example(metaclass=ExampleMeta):
    pass


print(Example.method)
print(Example.method())


class Example:
    @staticmethod
    def method():
        print('static!')


print(Example.method)
Example.method()