g = lambda x: x*x
a = lambda: 'example'
b = lambda x, y=3: x + y

print(g(8))
print(a())
print(b(5))
print(b(5, 1))