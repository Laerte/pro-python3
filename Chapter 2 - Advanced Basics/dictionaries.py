from collections import OrderedDict
from collections import defaultdict

'''
Ordered Dictionaries

The only reliable way to supply ordering to OrderedDict() 
is to use a standard sequence, such as a list or a generator expression.

'''

d = OrderedDict((value, str(value)) for value in range(10) if value > 5)

print(d)
d[10] = '10'
print(d)
del d[7]
print(d)

# Dictionaries with Defaults


def count_words(text):
    count = defaultdict(int)
    for word in text.split(' '):
        count[word] += 1

    return count


print(count_words('a b c'))
