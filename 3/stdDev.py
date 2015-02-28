def stdDevOfLengths(L):
    if len(L) == 0:
        return float('NaN')
    total = 0;
    mean = sum([len(elem) for elem in L])/float(len(L))
    for elem in L:
        total += pow((len(elem) - mean), 2)
    return pow((total/float(len(L))), 0.5)

def CoefOfVariant(L):
    total = 0;
    mean = sum([elem for elem in L])/float(len(L))
    for elem in L:
        total += pow((elem - mean), 2)
    return pow((total/float(len(L))), 0.5)/mean

print CoefOfVariant([10, 4, 12, 15, 20, 5])

#print stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples'])