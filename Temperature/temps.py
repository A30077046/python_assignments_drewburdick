def readTemps():
    file = open("temps.txt")
    temps = [];
    for line in file:
        temps.append(float(line))
    return temps

def calculateAve(temps, start, stop):
    index = 0
    total = 0
    for t in temps:
        if (index >= start and index < stop):
            total = total + t
        index = index + 1
    return total/(stop-start)

def count(temps, start, stop):
    index = 0
    c = 0
    for t in temps:
        if (index >= start and index < stop):
            if t > 0.0:
                c = c + 1
        index = index + 1
    return c

def main():
    temps = readTemps()
    chunk1 = int(len(temps)*0.70)
    count1a = calculateAve(temps, 0, chunk1);
    count1b = count(temps, 0, chunk1);
    count2a = calculateAve(temps, chunk1, len(temps));
    count2b = count(temps, chunk1, len(temps))
    print "During the first %s years, the average deviation from the temperature anomoly is %s" % (chunk1, count1a)
    print "During the first %s years, %s had a positive temperature anomaly" % (chunk1, count1b)
    print "During the last %s years, the average deviation from the temperature anomoly is %s" % (len(temps)-chunk1, count2a)
    print "During the last %s years, %s had a positive temperature anomaly" % (len(temps)-chunk1, count2b)

main()

