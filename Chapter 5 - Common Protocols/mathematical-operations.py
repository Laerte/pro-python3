class Example:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other


print(Example(10) + 20)

#  __truediv__()
print(5 / 4)

# __floordiv__(), floor division aka integer division
print(5 // 4)


print(20 // 6)

# __mod__(), modulo operation
print(20 % 6)


# variable interpretation
print('test%s' % 'ing')


def hours_and_minutes(minutes):
    return minutes // 60, minutes % 60


print(hours_and_minutes(60))
print(hours_and_minutes(137))
print(hours_and_minutes(42))


class Example:
    def __init__(self, value):
        self.value = value

    def __divmod__(self, divisor):
        return self.value // divisor, self.value % divisor


print(divmod(Example(20), 6))


class Example:
    def __init__(self, value):
        self.value = value

    def __pow__(self, power):  # exponentiation
        val = 1

        for x in range(power):
            val *= self.value

        return val


print(Example(5) ** 3)

print(5 ** 3)
print(125 % 50)
print(5 ** 3 % 50)
print(pow(5, 3, 50))


class Example:
    def __init__(self, value):
        self.value = value

    def __pow__(self, power, modulo=None):  # exponentiation
        val = 1

        for x in range(power):
            val *= self.value

        if modulo is not None:
            val %= modulo

        return val


print(Example(5) ** 3)
print(Example(5) ** 3 % 50)
print(pow(Example(5), 3, 50))

