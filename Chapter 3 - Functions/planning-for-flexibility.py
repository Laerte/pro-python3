def add_prefix(my_string, prefix='pro_'):
    """Adds a 'pro_' prefix before the new string is returned."""
    return prefix + my_string


final_string = input('Enter a string so we can put pro_ in front of it!: ')
print(add_prefix(final_string))
