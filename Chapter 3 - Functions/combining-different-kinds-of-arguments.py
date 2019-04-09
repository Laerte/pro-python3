# There are only four types of arguments; they generally appear in functions in this order:
#    - Required arguments
#    - Optional arguments
#    - Variable number of positional arguments
#    - Variable keyword arguments


def create_element(name, editable=True, *children, **attributes):
    pass

# Variable keyword arguments must be positioned at the end of the list, after all other types of arguments


def join_with_prefix(*segments, delimiter=' ', prefix):
    return delimiter.join(prefix + segment for segment in segments)


print(join_with_prefix('ro', 'ython', prefix='P'))
