def main():
    num = countBirds('Birds.txt')
    askUser(num)
def taskcall(call):
    print call,
    d = raw_input()
    return d
def countBirds(filename):
    d = {}
    for line in open(filename):
        temp = line.split(',')
        name = temp[0].strip()
        count = int(temp[1].strip())
        if name in d:
            d[name] = d[name] + count
        else:
            d[name] = count
    return d
def askUser(d):
    name = taskcall("Enter a birds name here:")
    sightings = 0
    if name in d:
        sightings = d[name]
    print "I've seen this bird %s time(s)." % sightings
    return sightings

main()