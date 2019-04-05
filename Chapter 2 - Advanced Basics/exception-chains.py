def get_value(dictionary, name):
    try:
        return dictionary[name]
    except Exception as e:
        print("exception hit..writing to file")
        log = open('logfile.txt', 'w')
        log.write('%s\n' % e)
        log.close()


#names = {"Jack": 113, "Jill": 32,"Yoda": 395}
#print(get_value(names, "Jackz"))  # change to Jack and it runs fine


def validate(value, validator):
    try:
        return validator(value)
    except Exception as e:
        raise ValueError('Invalid value: %s' % value) from e


def validator(value):
    if len(value) > 10:
        raise ValueError("Value can't exceed 10 characters")


validate('test', validator)
validate(False, validator)
