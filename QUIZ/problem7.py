import random
import pylab

def LV():
    balls = []
    for i in range(500):
        balls.append('w')
        balls.append('b')
    random.shuffle(balls)
    n = 1
    check = random.choice(balls)
    while check != 'w':
        check = random.choice(balls)
        n+=1
    return n

def MV():
    balls = []
    k=5
    for i in range(500):
        balls.append('w')
        balls.append('b')
    random.shuffle(balls)
    n = 1
    index = random.choice(range(len(balls)))
    check = balls[index]
    i=1
    while check != 'w':
        check = balls[(index+i)%len(balls)]
        n+=1
        i+=1
        if n==k:
            return 0
    return n


histogram = []  # intialize the list to be all zeros

for i in range(100):
    #histogram.append(LV())
    histogram.append(MV())


pylab.hist(histogram)
pylab.show()