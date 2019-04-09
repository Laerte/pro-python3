import os
import functools


def load_file(file, base_path='/', mode='rb'):
    return open(os.path.join(base_path, file), mode)


# partial application of the function "preloading arguments"
# return a new callable that can be used later
load_writable = functools.partial(load_file,
                                  mode='w',
                                  base_path='/Users/laerte/Projetos/pro-python3/Chapter 3 - Functions')

f = load_writable('example.txt')
print(f.mode)
f.close()
