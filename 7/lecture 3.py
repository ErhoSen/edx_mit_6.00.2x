import math
import numpy

def variance(lt):
    result = []
    for i in lt:
        result.append((numpy.mean(lt) - i)**2)
    return sum(result)

def badness(clusters):
    return sum([variance(lt) for lt in clusters])

C1 = [2, 2, 2]
C2 = [-6, -6, -4, -4]
c3 = [C1, C2]
print variance(C2)
print badness(c3)