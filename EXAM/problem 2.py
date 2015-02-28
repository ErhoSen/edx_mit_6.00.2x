import pylab

# a = 1.0
# b = 2.0
# c = 4.0
# yVals = []
# xVals = range(-20, 20)
# for x in xVals:
#     yVals.append(a*x**2 + b*x + c)
# yVals = 2*pylab.array(yVals)
# xVals = pylab.array(xVals)
# try:
#     a, b, c, d = pylab.polyfit(xVals, yVals, 3)
#     print round(a), b, c, d
# except:
#     print 'fell to here'

A = [0,1,2,3,4,5,6,7,8]

B = [5,10,10,10,15]

C = [0,1,2,4,6,8]

D = [6,7,11,12,13,15]

E = [9,0,0,3,3,3,6,6]

lists = [A, B, C, D, E]


def possible_mean(L):
    return sum(L)/len(L)

def possible_variance(L):
    mu = possible_mean(L)
    temp = 0
    for e in L:
        temp += (e-mu)**2
    return temp / len(L)

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return tot/len(X)

for elem in lists:
    print pylab.mean(elem), possible_mean(elem)
    print stdDev(elem), possible_variance(elem)
    print "\n"
