import pylab

inFile = open('julyTemps.txt', 'r')

result = []
ok = inFile.readlines()
for elem in ok:
    elem = elem[:-1].split(' ')
    if len(elem) < 3 or not elem[0].isdigit():
        continue
    result.append(elem)

high_temp = [elem[1] for elem in result]
low_temp = [elem[2] for elem in result]
diff_temp = [int(elem[1]) - int(elem[2]) for elem in result]
#pylab.plot(range(1, 32), high_temp)
#pylab.plot(range(1, 32), low_temp)
pylab.plot(range(1, 32), diff_temp)
pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
pylab.xlabel('Days')
pylab.ylabel('Temperature Ranges')
pylab.show()