import itertools

print(list(itertools.chain(range(3),
                           range(4, 6),
                           range(6, 11))))

# Zipping Iterables Together
print(list(zip(range(3), reversed(range(5)))))

keys = map(chr, range(97, 102))
values = range(1, 6)

print(dict(zip(keys, values)))
