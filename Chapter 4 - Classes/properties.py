class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def name(self):
        return '{}, {}'.format(self.last_name, self.first_name)

    @name.setter
    def name(self, value):
        self.last_name, self.first_name = value.split(',')

    @name.deleter
    def name(self):
        del self.first_name
        del self.last_name


p = Person('Laerte', 'Pereira')
print(p.name)

p.name = 'Pereira,Joao'
print(p.name)

del p.name

try:
    print(p.name)
except AttributeError as e:
    print(str(e))
