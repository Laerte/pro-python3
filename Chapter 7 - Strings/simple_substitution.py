def func(*args):
    for i, arg in enumerate(args):
        print('Argument %s: %r' % (i, arg))


func('example', {}, [1, 2, 3], object())


def log(*args):
    for i, arg in enumerate(args):
        print('Argument %(i)s: %(arg)r' % {'i': i, 'arg': arg})


log('test')
log('test', 'ing')