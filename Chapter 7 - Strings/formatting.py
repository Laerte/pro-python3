import datetime
import os.path

print('This is argument 0: {0}'.format('test'))
print('This is argument key: {key}'.format(key='value'))


def exact_match(expected, error):
    def validator(value):
        if value != expected:
            raise ValueError(error.format(value, expected))

    return validator


validate_zero = exact_match(0, 'Expected {1}, got {0}')

try:
    validate_zero(1)
except Exception as e:
    print(e)


def format_time(time):
    return '{0.minute} past {0.hour}'.format(time)


print(format_time(datetime.time(8, 10)))
print('{0[spam]}'.format({'spam': 'eggs'}))

validate_test = exact_match('test', 'Expected {1!r}, got {0!r}')
try:
    validate_test('invalid')
except Exception as e:
    print(e)


print('{0:>20}{1}'.format(*os.path.splitext('contents.txt')))

for filename in ['contents.txt', 'chapter.txt', 'index.txt']:
    print('{0:<10}{1}'.format(*os.path.splitext(filename)))


def heading(text, padding='=', width=40):
    return '{1}{0:{1}^{2}}{1}'.format(text, padding, width - 2)


print(heading('Standard Format Specification'))
print(heading('Standard Format Specification', padding='-', width=60))

contents = (('Installation', 20), ('Usage', 112))


def format_contents(contents):
    for title, line_number in contents:
        yield '{0:.<70}{1:.>5}'.format(title, line_number)


for line in format_contents(contents):
    print(line)


class Verb:
    def __init__(self, present, past=None):
        self.present = present
        self.past = past

    def __format__(self, tense):
        if tense == 'past':
            return self.past
        else:
            return self.present


format = Verb('format', past='formatted')
message = 'You can {0:present} strings with {0:past} objects.'
print(message.format(format))

save = Verb('save', past='saved')
print(message.format(save))