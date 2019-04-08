from example import *

public_func()

try:
    utility_func()  # trying to use a function that is not imported raise a NameError exception
except NameError:
    from example import utility_func

    utility_func()