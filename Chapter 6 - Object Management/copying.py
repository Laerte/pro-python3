import copy

a = [1, 2, 3]
b = a[:]  # copy

print(f"{id(a)}\n{id(b)}")

b.append(4)
print(f"{b}\n{a}")

a = {1: 2, 3: 4}
b = a.copy()
b[5] = 6

print(f"{b}\n{a}")

# Shallow Copies


class Example:
    def __init__(self, value):
        self.value = value


a = Example('spam')
b = copy.copy(a)
b.value = 'eggs'
print(f"{a.value}\n{b.value}")

a = {'a': [1, 2, 3], 'b': [4, 5, 6]}
b = a.copy()
a['a'].append(4)  # Copy to a and b
b['b'].append(7)  # Copy to a and b
print(f"{a}\n{b}")


# Deep copies


original = [[1, 2, 3], [1, 2, 3]]
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)
original[0].append(4)

print(f"{shallow_copy}\n{deep_copy}")

a = [1, 2, 3]
b = [a, a]
print(b)

b[0].append(4)
print(b)

c = copy.deepcopy(b)
c[0].append(5)
# copied structure will have the same behavior
# as the original with regard
# to how changes are reflected in referenced objects
print(c)
