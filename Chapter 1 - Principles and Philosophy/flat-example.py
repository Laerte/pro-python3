x = 1
y = 399


def checker(x, y):
    if x > 0:
        if y > 100:
            raise ValueError("Value for y is too large.")
        else:
            return y


print(checker(x, y))
