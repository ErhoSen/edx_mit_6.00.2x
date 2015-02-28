# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b_precompiled_27 import *

#
# PROBLEM 1
#

def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    delayTimes = [150]

    # 'delayTime' represents the number of hours the simulation is run before the drug 'guttagonol' is administered
    for delayTime in delayTimes:
        totVirusPops = []
        # runs 'numTrials' number of trials for each 'delayTime',
        for trial in xrange(numTrials):

            # creates a list of 100 'ResistantVirus' instances,
            viruses = []
            for i in xrange(100):
                viruses.append(ResistantVirus(1.0,0.05,{'guttagonol':False},0.005))

            # intantiates a 'Patient' instance,
            p = TreatedPatient(viruses,1000)

            # runs the stimulation for 'delayTime' number of time-steps,
            for before in xrange(delayTime):
                p.update()

            # administers the drug 'guttagonol',
            p.addPrescription('guttagonol')

            # runs the simulation for another 150 time-steps,
            for after in xrange(150):
                p.update()
            # records the total virus population at end of trial,
            totVirusPops.append(p.getTotalPop())
        # draws a histogram of final virus populations for each 'dalayTime'.
        pylab.figure()
        pylab.hist(totVirusPops)
        pylab.legend()
        pylab.xlabel('Final virus Population')
        pylab.ylabel('Frequency')
        pylab.title('Final virus populations. Treatment is delayed by ' + str(delayTime) + ' hours')

    pylab.show()


#simulationDelayedTreatment(10)

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    delayTimes =(0, 75, 150, 300)

    # 'delayTime' represents the number of hours the simulation is run before the drug 'guttagonol' is administered
    for delayTime in delayTimes:
        totVirusPops = []
        cured = 0.0
        # runs 'numTrials' number of trials for each 'delayTime',
        for trial in xrange(numTrials):

            # creates a list of 100 'ResistantVirus' instances,
            viruses = []
            for i in xrange(100):
                viruses.append(ResistantVirus(1.0,0.05,{'guttagonol': False, 'grimpex': False},0.005))

            # intantiates a 'Patient' instance,
            p = TreatedPatient(viruses,1000)

            #run 150 times
            for t in xrange(150):
                p.update()

            p.addPrescription('guttagonol')

            # runs the stimulation for 'delayTime' number of time-steps,
            for before in xrange(delayTime):
                p.update()

            # administers the drug 'qrimpex',
            p.addPrescription('grimpex')

            # runs the simulation for another 150 time-steps,
            for after in xrange(150):
                p.update()
            # records the total virus population at end of trial,
            totVirusPops.append(p.getTotalPop())
            # if the total virus population is less than 50, the 'cured' counter is incremented by 1,
            if p.getTotalPop() < 50:
                cured += 1

        # calculates and prints the percentage of trials where the total virus population was less than 50 at the end
        curedPercent = (cured/ numTrials) * 100
        print 'Number of cured patients: ', str(curedPercent)

        # draws a histogram of final virus populations for each 'dalayTime'.
        pylab.figure()
        pylab.hist(totVirusPops)
        pylab.legend()
        pylab.xlabel('Final virus Population')
        pylab.ylabel('Frequency')
        pylab.title('Final virus populations. Treatment is delayed by ' + str(delayTime) + ' hours')

    pylab.show()

simulationTwoDrugsDelayedTreatment(30)