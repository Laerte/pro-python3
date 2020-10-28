class Range:
    def __init__(self, count):
        self.count = count
    def __getitem__(self, index):
        if index < self.count:
            return index
        raise IndexError

def range_gen(count):
    for x in range(count):
        yield x

r = range_gen(5)
print(list(r))
print(list(r))

r = Range(5)
print(list(r))
print(list(r))
