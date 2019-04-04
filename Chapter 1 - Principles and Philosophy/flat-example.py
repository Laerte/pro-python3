x = 1
y = 399


def checker(x, y):
    if x > 0 and y > 100:
        raise ValueError("Value for y is too large.")
    elif x > 0:
        return y
    elif x == 0:
        return False
    else:
        raise ValueError("Value for x cannot be negative.")


print(checker(x, y))
