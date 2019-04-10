import functools


def memoize(func): # Memoization is best suited for functions with a few arguments
    """
    Cache the results of the function so it doesn't need to be called
    again, if the same arguments are provided a second time.
    """
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]

        # This line is for demonstration only.
        # Remove it before using it for real.
        print('Calling %s()' % func.__name__)
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@memoize
def multiply(x, y):
    return x * y


@memoize
def factorial(x):
    result = 1

    for i in range(x):
        result *= i + 1

    return result


print(multiply(2,5))
print(multiply(2,5))
print(factorial(5))
print(factorial(5))
