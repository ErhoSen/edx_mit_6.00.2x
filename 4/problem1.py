import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    # Your code here
    success = 0.0
    for i in range(numTrials):
        bucket = ['g', 'g', 'g', 'r', 'r', 'r']
        for j in range(3):
            rand_i = random.randrange(0,len(bucket))
            bucket.pop(rand_i)
        if bucket[0] == bucket[1] == bucket[2]:
            success+=1
    return success/numTrials

print noReplacementSimulation(1000)