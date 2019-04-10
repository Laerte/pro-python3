import functools


def suppress_errors(func):
    """Automatically silence any errors that occur within a function"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            pass

    return wrapper


@suppress_errors
def sum_numbers(x, y):
    return x + y


def multiply_by(factor):  # Closure
    """Return a function that multiplies values by the given factor"""
    def multiply(value):
        """Multiply the given value by the factor already provided"""
        return value * factor

    return multiply


times2 = multiply_by(3)

print(times2(2))
print(sum_numbers(1, None))
