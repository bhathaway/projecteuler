def validTriple(t, max_value):
    return t[0] < t[1] and t[1] < t[2] and t[2] <= max_value

def nextTripleWithSameSum(trip, max_value):
    t = trip
    m = max_value
    assert(validTriple(t, m))

    result = [t[0], t[1]+1, t[2]-1]
    if validTriple(result, m):
        return result

    candidate_t2 = sum(t) - 2*t[0] - 3
    if candidate_t2 < m:
        result = [t[0]+1, t[0]+2, sum(t)-2*t[0]-3]
        if validTriple(result, m):
            return result
    else:
        result = [t[0]+1, sum(t)-m-t[0]-1, m]
        if validTriple(result, m):
            return result

    return None

# This function will generate a map from
# sums to lists of 3 increasing integers
# adding to that sum.
def getMagicTriples(max_number):
    pass # Work in progress.
    result = {}

    # First process is to seed the iterator.
    iterator = [1, 2, 3]
    s = sum(iterator)
