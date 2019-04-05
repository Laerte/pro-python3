import logging


def count_lines(filename):
    """
    Count the number of lines in a file. If the file can't be
    opened, it should be treated the same as if it was empty.
    """
    try:
        return len(open(filename, 'r').readlines())
    except (EnvironmentError, TypeError) as e:
        print('exception error reading the file or calculating lines!')
        # Something went wrong reading the file
        logging.error(e)
        # or calculating the number of lines.
        return 0


myfile = input('Enter a file to open: ')
print(count_lines(myfile))
