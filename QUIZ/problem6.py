def probTest(limit):
    n = 1
    prob = 1/6.0
    while prob > limit:
        n += 1
        prob = (5.0**(n - 1))/(6.0**(n))
    return n


def probTest(limit):
    prob = 1/6.0
    rolls = 0
    while prob > limit:
        rolls+=1
        prob*=5.0/6.0
        #print "Chance:", prob
        #print "Rolls:", rolls
    return rolls

limit = 1.0/6.0
print "LIMIT", limit
print probTest(limit)