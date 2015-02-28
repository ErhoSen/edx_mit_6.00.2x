import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    for rabbit in range(CURRENTRABBITPOP):
        rabbit_repr_prob = 1.0 - CURRENTRABBITPOP/float(MAXRABBITPOP)
        if random.random() <= rabbit_repr_prob and CURRENTRABBITPOP <= 1001:
            #print "SUCCESS", rabbit_repr_prob
            CURRENTRABBITPOP += 1


def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    for fox in range(CURRENTFOXPOP):
        prob_fox_eat_rabbit = CURRENTRABBITPOP/float(MAXRABBITPOP)
        if random.random() <= prob_fox_eat_rabbit and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP-=1
            fox_repr_prob = 1/float(3)
            if random.random() <= fox_repr_prob:
                CURRENTFOXPOP+=1
        if random.random() <= 0.9 and CURRENTFOXPOP > 10:
            CURRENTFOXPOP -= 1


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_populations = []
    fox_populations = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return rabbit_populations, fox_populations


rabbit_populations, fox_populations = runSimulation(200)
rab_coeff = pylab.polyfit(range(len(rabbit_populations)), rabbit_populations, 2)
pylab.plot(pylab.polyval(rab_coeff, range(len(rabbit_populations))), label='rabbit curve')

fox_coeff = pylab.polyfit(range(len(fox_populations)), fox_populations, 2)
pylab.plot(pylab.polyval(fox_coeff, range(len(fox_populations))), label='fox curve')

#pylab.plot(xrange(0, len(rabbit_populations)), rabbit_populations, label='Rabbit Population')
#pylab.plot(xrange(0, len(fox_populations)), fox_populations, label='Fox Population')
pylab.title('Forest Games Simulation')
pylab.xlabel('time step')
pylab.ylabel('# animals')
pylab.legend(loc='best')
pylab.show()