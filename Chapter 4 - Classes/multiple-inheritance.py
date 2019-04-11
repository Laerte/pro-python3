# Mixin classes don’t provide full functionality on their own; they instead supply
# just a small add-on feature that could be useful on a wide range of different classes, eg:


class NoneAttributes:
    def __getattr__(self, name):
        return None


class BaseClass:
    pass


class Example(BaseClass, NoneAttributes):
    pass


e = Example()
print(e.does_not_exist)
