import inspect


def example(a=1, b=1, *c, d, e=2, **f) -> str:
    pass


def get_arguments(func, args, kwargs):
    """
    Given a function and a set of arguments, return a dictionary
    of argument values that will be sent to the function.
    """
    arguments = {}
    spec = inspect.getfullargspec(func)

    if spec.defaults:
        arguments.update(zip(reversed(spec.args), reversed(spec.defaults)))

    if spec.kwonlydefaults:
        arguments.update(spec.kwonlydefaults)

    arguments.update(zip(spec.args, args))
    arguments.update(kwargs)

    return arguments


print(get_arguments(example, (1,), {'f': 4}))


def validate_arguments(func, args, kwargs):
    """
    Given a function and its arguments, return a dictionary
    with any errors that are posed by the given arguments.
    """
    arguments = get_arguments(func, args, kwargs)
    spec = inspect.getfullargspec(func)
    declared_args = spec.args[:]
    declared_args.extend(spec.kwonlyargs)
    errors = {}

    for name in declared_args:
        if name not in arguments:
            errors[name] = "Required argument not provided."

    for name in arguments:
        if name not in declared_args:
            errors[name] = "Unknown argument provided."

    return errors


print(validate_arguments(example, (1,), {'f': 4}))
