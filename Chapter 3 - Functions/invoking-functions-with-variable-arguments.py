# A single asterisk specifies positional arguments, while two asterisks specify keyword arguments.


def join_with_prefix(*segments, delimiter=' ', prefix):
    return delimiter.join(prefix + segment for segment in segments)


value = 'ro ython'

print(join_with_prefix(*value.split(' '), prefix='P'))
