import random

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    random.seed(0) # This will be discussed in the video "Drunken Simulations"
    return 2 * random.randint(5, 10)

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.randrange(10, 21, 2)

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    return random.choice([i for i in range(100) if i%2==0])


