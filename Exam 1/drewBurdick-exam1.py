def readData(filename):
    l = []
    file = open(filename)
    for speed in file:
        l.append(int(speed.strip()))
    return l

def getAverage(l):
    total = 0.00
    for speed in l:
        total = total + speed
    return total/len(l)

def countSpeeders(l, maxSpeed):
    count = 0
    for speed in l:
        if speed >= maxSpeed:
            count = count + 1
    return count

def main():
    rush = readData("data-rush.txt")
    norush = readData("data-not-rush.txt")
    avrush = getAverage(rush)
    avnorush = getAverage(norush)
    rushnum = countSpeeders(rush, 70)
    norushnum = countSpeeders(norush, 70)
    print "The average speed during rush hour was %.2f." % avrush
    print "The average speed not during rush hour was %.2f." % avnorush
    print "There were %s speeders during rush hour. Total fine = $%s" % (rushnum, rushnum*150) 
    print "There were %s speeders not during rush hour. Total fine = $%s" % (norushnum, norushnum*100)

main()