from importlib import import_module

print(import_module('os.path'))
print(import_module('os'))
print(import_module('example', package=__name__))
