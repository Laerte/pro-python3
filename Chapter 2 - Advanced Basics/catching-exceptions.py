import logging


def count_lines(filename):
    """
    Count the number of lines in a file. If the file can't be
    opened, it should be treated the same as if it was empty.
    """
    try:
        file = open(filename, 'r')
    except TypeError as e:
        # The filename wasn't valid for use with the filesystem.
        logging.error(e)
    except EnvironmentError as e:
        # Something went wrong reading the file
        logging.error(e.args[1])
        return 0
    else:
        return len(file.readlines())


myfile = input('Enter a file to open: ')
print(count_lines(myfile))
