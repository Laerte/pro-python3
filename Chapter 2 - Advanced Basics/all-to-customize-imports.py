from example import *

'''
EXPLICIT IS BETTER THAN IMPLICIT

It’s generally considered bad form to import using the asterisk notation.
PEP 8, the Python Style Guide, specifically recommends against it. 
'''

public_func()

try:
    utility_func()  # trying to use a function that is not imported raise a NameError exception
except NameError:
    from example import utility_func

    utility_func()