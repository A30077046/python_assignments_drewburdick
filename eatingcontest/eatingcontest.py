import random
import time

def winner(contestA, contestB, contestC):
    if (contestA > 50 and contestA > contestB and contestA > contestC):
        return "Tom!"
    elif (contestB > 50 and contestB > contestA and contestB > contestC):
        return "Sally"
    elif (contestC > 50 and contestC > contestA and contestC > contestB):
        return "Fred"
    else:
        return ""
        
def inputUser(prompt):
    print prompt,
    userinput = raw_input()
    return userinput
    
def announce(pred, champ):
    print 
    if pred == champ:
        print "You guessed right, %s wins!" % champ
    else:
        print "Nice try, but %s is top dog!" % champ

def main():
    champ = ""
    contestA = 0
    contestB = 0
    contestC = 0
    
    pred = inputUser("Print winner's name here (Tom, Sally, or Fred)")
    print "Ready, set, eat!"
    
    while champ == "":
        contestA = contestA + random.randrange(1, 6)
        contestB = contestB + random.randrange(1, 6)
        contestC = contestC + random.randrange(1, 6)

        print "chomp...  chomp...  chomp... ",
        print ""
        time.sleep(1)
        print "Tom has eaten %s hot dogs!" % contestA
        print "Sally has eaten %s hot dogs!" % contestB
        print "Fred has eaten %s hot dogs!" % contestC
        champ = winner(contestA, contestB, contestC)
        
    announce(pred, champ)

        
main()