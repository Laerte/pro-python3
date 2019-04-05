def count_lines(filename):
    """
    Count the number of lines in a file.
    """

    with open(filename, 'r') as file:
        return len(file.readlines())


myfile = input('Enter a file to open: ')
print(count_lines(myfile))
