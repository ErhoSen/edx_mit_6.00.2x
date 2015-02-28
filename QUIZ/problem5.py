import random
import pylab

def sampleQuizzes():
    ok = 0.0
    for t in range(10000):
        mid1 = random.randint(50, 80)*0.25
        mid2 = random.randint(60, 90)*0.25
        fin = random.randint(55, 95)*0.50
        score = mid1+mid2+fin
        if 70 <= score <= 75:
            ok+=1.0
    return ok/10000.0

def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of
    the three exams, then calculates the final score and
    appends it to a list of scores.

    Returns: A list of numTrials scores.
    """
    scores = []
    for t in range(numTrials):
        mid1 = random.randint(50, 80)*0.25
        mid2 = random.randint(60, 90)*0.25
        fin = random.randint(55, 95)*0.50
        score = mid1+mid2+fin
        scores.append(score)
    return scores

def plotQuizzes():
    scores = generateScores(10000)
    pylab.hist(scores, bins=7)
    pylab.title('Distribution od Scores')
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    #pylab.legend('best')
    pylab.show()

#plotQuizzes()