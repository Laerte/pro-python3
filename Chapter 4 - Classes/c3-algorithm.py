import itertools


def C3(cls, *mro_lists):
    # Make a copy so we don't change existing content
    mro_lists = [list(mro_list[:]) for mro_list in mro_lists]
    # Set up the new MRO with the class itself
    mro = [cls]
    # The real algorithm goes here.

    while True:
        # Reset for next round of tests
        candidate_found = False

        for mro_list in mro_lists:
            if not len(mro_list):
                # Any empty lists are of no use to the algorithm
                continue

            # Get the first item as a potential candidate for the MRO.
            candidate = mro_list[0]

            if candidate_found:
                # Candidates promoted to the MRO are no longer of use.
                if candidate in mro:
                    mro_list.pop(0)
                # Don't bother checking any more candidates if one was found.
                continue

            if candidate in itertools.chain(*(x[1:] for x in mro_lists)):
                # The candidate was found in an invalid position, so we
                # move on to the next MRO list to get a new candidate.
                continue
            else:
                # The candidate is valid and should be promoted to the MRO.
                mro.append(candidate)
                mro_list.pop(0)
                candidate_found = True

        if not sum(len(mro_list) for mro_list in mro_lists):
            # There are no MROs to cycle through, so we're all done.
            # note any() returns false if no items so it could replace sum(len)
            break

        if not candidate_found:
            # No valid candidate was available, so we have to bail out.
            raise TypeError("Inconsistent MRO")

    return mro


print(C3('C', ['B', 'A', 'object'], ['A', 'object'], ['B', 'A']))
print(C3('C', ['B', 'A', 'object'], ['A', 'object']))
print(C3('C', ['A', 'object'], ['B', 'A', 'object']))

try:
    print(C3('C', ['A', 'B', 'object'], ['B', 'A', 'object'], ['A', 'B']))
except TypeError as e:
    print(str(e))  # Inconsistent MRO

# Python’s class system disallows this construct in an effort to force
# developers to only make classes that make sense
try:
    class A:
        pass


    class B(A):
        pass

    class C(A, B):
        pass
except TypeError as e:
    print(str(e))

