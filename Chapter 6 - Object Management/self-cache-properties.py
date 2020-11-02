class Example:
    @property
    def attr(self):
        if 'attr' not in self.__dict__:
            # Do the real work of retrieving the value
            print('Getting value')
            self.__dict__['attr'] = 42
        return self.__dict__['attr']


example = Example()

print(example.attr)
print(example.attr)
