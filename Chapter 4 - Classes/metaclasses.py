class SimpleMetaclass(type):
    def __init__(cls, name, bases, attrs):
        print(name)
        super(SimpleMetaclass, cls).__init__(name, bases, attrs)


class Example(metaclass=SimpleMetaclass):
    pass


class PluginMount(type):
    """
    Place this metaclass on any standard Python class to turn it into a plugin
    mount point. All subclasses will be automatically registered as plugins.
    """

    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'plugins'):
            # The class has no plugins list, so it must be a mount point,
            # so we add one for plugins to be registered in later.
            cls.plugins = []
        else:
            # Since the plugins attribute already exists, this is an
            # individual plugin, and it needs to be registered.
            cls.plugins.append(cls)


class InputValidator(metaclass=PluginMount):
    """
    A plugin mount for input validation.
    Supported plugins must provide a validate(self, input) method, which
    receives
    input as a string and raises a ValueError if the input was invalid. If the
    input was properly valid, it should just return without error. Any return
    value will be ignored.
    """

    def validate(self, input):
        # The default implementation raises a NotImplementedError
        # to ensure that any subclasses must override this method.
        raise NotImplementedError


class ASCIIValidator(InputValidator):
    """
    Validate that the input only consists of valid ASCII characters.
    >>> v = ASCIIValidator()
    >>> v.validate('sombrero')
    >>> v.validate('jalapeño')
    Traceback (most recent call last):
    ...
    UnicodeDecodeError: 'ascii' codec can't decode character '\xf1' in position
    6: ordinal not in range(128)
    """
    def validate(self, input):
        # If the encoding operation fails, str.enc ode() raises a
        # UnicodeDecodeError, which is a subclass of ValueError.
        input.encode('ascii')


def is_valid(input):
    for plugin in InputValidator.plugins:
        try:
            plugin().validate(input)
        except ValueError as e:
            # A ValueError means invalidate input
            return False

    # All validators succeeded
    return True


print(InputValidator().plugins)

print(is_valid('sobrero'))
print(is_valid('jalapeño'))
