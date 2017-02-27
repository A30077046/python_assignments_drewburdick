def main():
    timingList = order("timings.txt")
    dis(timingList)
    
skill = ["Cube Head (0 - 9.99)",
        "Square Master (10 - 19.99)",
        "Advanced Twister (20 - 29.99)",
        "Intermediate Turner (30 - 39.99)",
        "Average Mover (40 - 59.99)",
        "Pathetic (60 and beyond)"]
        
def order(file):
    timingList = {}
    for level in range(0, 6):
        timingList[skill[level]] = []
        
    read = open(file)
    for line in read:
        breakList = line.split(",")
        ind = breakList[0].strip();
        sec = float(breakList[1].strip());
        if sec <= 10:
            timingList[skill[0]].append(ind)
        elif sec <= 20:
            timingList[skill[1]].append(ind)
        elif sec <= 30:
            timingList[skill[2]].append(ind)
        elif sec <= 40:
            timingList[skill[3]].append(ind)
        elif sec <= 60:
            timingList[skill[4]].append(ind)
        else:
            timingList[skill[5]].append(ind)
    return timingList;       
    
def dis(timingList):
    for k in skill:
        print "%s: " % k
        for t in timingList[k]:
            print "%s" % t
main()