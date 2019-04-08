def unique_letters(word):
    return set(word.lower())


print(unique_letters('eggs'))

example = {1, 2, 3, 4, 5}

print(example)

example.add(6)

print(example)

example.update({6, 7, 8, 9})

print(example)

example.remove(9)  # raise 'KeyError' exception if item don't exists on set

print(example)

example.discard(8)

print(example)

example.discard(8)  # don't raise exception, just remove the item.

print(example)

print(example.pop())

print(example)

example.clear()  # remove all items

print(example)

print({1, 2, 3} | {4, 5, 6})  # union

print({1, 2, 3}.union({4, 5, 6}))  # union

print({1, 2, 3, 4, 5} & {4, 5, 6, 7, 8})  # intersection

print({1, 2, 3, 4, 5}.intersection({4, 5, 6, 7, 8}))  # intersection

print({1, 2, 3, 4, 5} - {2, 4, 6})  # difference

print({1, 2, 3, 4, 5}.difference({2, 4, 6}))  # difference

print({1, 2, 3, 4, 5} ^ {4, 5, 6})  # symmetric difference, all items that were in either set, but not in both

print({1, 2, 3, 4, 5}.symmetric_difference({4, 5, 6}))  # symmetric difference

'''
    If one set contains all the items of another, the first is considered to be a
    superset of the other, even if the first set contains additional items not present in the
    second. The inverse, where all the items in first are contained in the second, even if the
    second has more items, means the first set is a subset of the second.
'''

print({1, 2, 3}.issubset({1, 2, 3, 4, 5}))

print({1, 2, 3, 4, 5}.issubset({1, 2, 3}))

print({1, 2, 3}.issuperset({1, 2, 3, 4, 5}))

print({1, 2, 3, 4, 5}.issuperset({1, 2, 3}))

print(not ({1, 2, 3} - {1, 2, 3, 4, 5}))

print(not ({1, 2, 3, 4, 5} - {1, 2, 3}))
