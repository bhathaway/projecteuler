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

