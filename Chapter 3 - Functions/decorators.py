import functools


def suppress_errors(func=None, log_func=None):
    """Automatically silence any errors that occur within a function"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if log_func is not None:
                    log_func(str(e))

        return wrapper

    if func is None:
        return decorator
    else:
        return decorator(func)


def print_logger(message):
    print(message)


@suppress_errors(log_func=print_logger)
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
