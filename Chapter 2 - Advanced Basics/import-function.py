import sys


def import_child(module_name):
    __import__(module_name)

    return sys.modules[module_name]

print(import_child('os.path'))
print(import_child('os'))
