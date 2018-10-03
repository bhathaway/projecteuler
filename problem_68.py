def validTriple(t, max_value):
    return t[0] < t[1] and t[1] < t[2] and t[2] <= max_value

def triplesWithSum(s, max_value):
    m = max_value
    t = [1, 2, s-3]
    if t[2] > max_value:
        t[1] += t[2] - max_value
        t[2] = max_value
    if not validTriple(t, m):
        return

    yield t

    while t != None:
        result = [t[0], t[1]+1, t[2]-1]
        if validTriple(result, m):
            yield result
            t = result
            continue

        candidate_t2 = sum(t) - 2*t[0] - 3
        if candidate_t2 < m:
            result = [t[0]+1, t[0]+2, sum(t)-2*t[0]-3]
            if validTriple(result, m):
                yield result
                t = result
                continue
        else:
            result = [t[0]+1, sum(t)-m-t[0]-1, m]
            if validTriple(result, m):
                yield result
                t = result
                continue

        result = None
        t = result
        continue


class PolygonRing:
    def __init__(self, outer_ring, inner_ring):
        N = len(outer_ring)
        assert(N >= 3)
        assert(len(inner_ring) == N)
        
        found_i = [False for _ in range(2*N)]
        for x in outer_ring:
            assert(not found_i[x-1])
            found_i[x-1] = True
        for x in inner_ring:
            assert(not found_i[x-1])
            found_i[x-1] = True

        self._outer_ring = outer_ring
        self._inner_ring = inner_ring
        self._n = N

    def getTriple(self, i):
        assert(i < self._n)
        return [self._outer_ring[i], self._inner_ring[i], self._inner_ring[(i+1)%self._n]]

    def isMagic(self):
        first_sum = sum(self.getTriple(0))
        for i in range(self._n):
            if sum(self.getTriple(i)) != first_sum:
                return False
        return True

    def __str__(self):
        result = ""
        for i in xrange(self._n - 1):
            t = self.getTriple(i)
            result += "{},{},{}; ".format(t[0], t[1], t[2])
        t = self.getTriple(self._n - 1)
        result += "{},{},{}".format(t[0], t[1], t[2])
        return result

    def getNumber(self):
        s = ""
        for i in xrange(self._n):
            t = self.getTriple(i)
            s += "{}{}{}".format(t[0], t[1], t[2])
        return int(s)

    def lowestForm(self):
        s = self._outer_ring.index(min(self._outer_ring))
        o = self._outer_ring
        i = self._inner_ring
        return PolygonRing(o[s:]+o[0:s], i[s:]+i[0:s])

    def __repr__(self):
        return self.__str__()

def testRings():
    ring1 = PolygonRing([4, 5, 6], [2, 3, 1])
    assert(ring1.isMagic())
    
# This function will generate a map from
# sums to lists of 3 increasing integers
# adding to that sum.
def getMagicTriples(max_number):
    result = {}
    for n in range(6, max_number*2 + 1):
        result[n] = list(triplesWithSum(n, max_number))
    return result

# I have a lot of groundwork set up now. I should decide my basic strategy
# for generating magic ngons. The idea is to iterate through the possible triples
# as starting points. An initial difficulty is that there are six arrangements
# of the triples. Assuming a configuration has been chosen, the next step is to
# proceed clockwise, realizing that the middle value for the next triple has
# been chosen. This has a couple benefits. One, we can eliminate all triples
# that do not have this number, and additionally, there are now only two configurations
# that the remaining triples can have. It's not actually that bad of a search space.
# I also need to remember that what will further constrain the space is that
# the other numbers besides the middle cannot have been seen previously.

# One particular question is that, since these are rings, how do I avoid
# over-solving the space? Maybe there's a way to take advantage of the
# symmetry somehow. Let me just try it out on the 3-gon ring and see if I
# can make it work, even if it is over-solved.

def backsolve(N, current_list, remaining):
    assert(len(current_list) <= N)

    if len(current_list) == N:
        outer_ring = []
        inner_ring = []
        for triple in current_list:
            outer_ring.append(triple[0])
            inner_ring.append(triple[1])

        try:
            p = PolygonRing(outer_ring, inner_ring)
            if p.isMagic():
                yield p
            raise StopIteration
        except AssertionError:
            raise StopIteration

    if remaining == []:
        raise StopIteration

    mid_element = current_list[-1][2]
    candidates = []
    for r in remaining:
        if mid_element in r:
            candidates.append(r)

    for i in xrange(len(candidates)):
        c = candidates[i]
        r_idx = remaining.index(c)
        assert(mid_element in c)
        idx = c.index(mid_element)
        right_idx = (idx + 1) % 3
        left_idx = (idx + 2) % 3
        candidate1 = [[c[left_idx], c[idx], c[right_idx]]]
        candidate2 = [[c[right_idx], c[idx], c[left_idx]]]

        for soln in backsolve(N, current_list + candidate1, remaining[0:r_idx] + remaining[r_idx+1:]):
            yield soln
        for soln in backsolve(N, current_list + candidate2, remaining[0:r_idx] + remaining[r_idx+1:]):
            yield soln

def magicNgon(N):
    max_number = 2 * N
    sum_to_triples = getMagicTriples(max_number)
    for s in sum_to_triples:
        triples = sum_to_triples[s]
        if len(triples) < N:
            continue
        for i in xrange(len(triples)):
            t = triples[i]
            for soln in backsolve(N, [[t[0], t[1], t[2]]], triples[0:i] + triples[i+1:]):
                yield soln
            for soln in backsolve(N, [[t[1], t[2], t[0]]], triples[0:i] + triples[i+1:]):
                yield soln
            for soln in backsolve(N, [[t[2], t[0], t[1]]], triples[0:i] + triples[i+1:]):
                yield soln
            for soln in backsolve(N, [[t[1], t[0], t[2]]], triples[0:i] + triples[i+1:]):
                yield soln
            for soln in backsolve(N, [[t[1], t[2], t[0]]], triples[0:i] + triples[i+1:]):
                yield soln
            for soln in backsolve(N, [[t[2], t[1], t[0]]], triples[0:i] + triples[i+1:]):
                yield soln

solutions = []
for m in magicNgon(5):
    n = m.lowestForm().getNumber()
    if n not in solutions:
        solutions.append(n)

solutions.sort()
for s in solutions:
    print s

