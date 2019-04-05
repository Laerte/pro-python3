def echo():
    """Returns everything you type until you press Ctrl-C"""

    while True:
        try:
            print(input('Type Something or CTRL C to exit: '))
        except KeyboardInterrupt:
            print()  # Make sure the prompt appears on a new line.
            print('bye for now...:')
            break


echo()
