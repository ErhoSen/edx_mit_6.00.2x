import pylab
import random

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
	wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
	tot += (x - mean)**2
    return (tot/len(X))**0.5

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vowels_list = "aeiou"
    vowels_ratios = []
    for word in wordList:
	counter = 0
	for ch in word:
	    if ch in vowels_list:
		counter+=1
	vowels_ratios.append(counter/float(len(word)))
    #print vowels_num[0:100]
    #ratios = vovel_ratio(vowels_num)
    #print vowels_ratios[0:100]
    #srd_dev = stdDev(vowels_ratios)
    #print srd_dev
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    print 'x-range =', xmin, '-', xmax
    print 'y-range =', ymin, '-', ymax
    pylab.hist(vowels_ratios, bins = numBins)
    pylab.show()

def test1():
    vals = []
    for i in range(100000):
	num = random.random()
	vals.append(num)
    pylab.hist(vals, bins = 11)
    pylab.show()

if __name__ == '__main__':
    #test1()
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
