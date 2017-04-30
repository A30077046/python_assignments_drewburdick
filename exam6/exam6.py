suspects = ["Miss Scarlet", "Col Mustard", "Mister Green"] #listing outcomes
weapons = ["Candlestick", "Wrench", "Pipe"] # listing oucomes


def generateOutcome(): # compiles list of possible outcomes
    outcomes = []
    for weapon in weapons:
        for suspect in suspects:
            outcome = {};
            outcome["weapon"] = weapon
            outcome["suspect"] = suspect
            outcomes.append(outcome)
    return outcomes
    
def input(outcomes): #raw input of hints
    ret = []
    print "Is the clue about a weapon or a suspect (w or s)?"
    typ = raw_input()
    if typ.upper() == "W":
        print "Enter the weapon that was not used (%s):" % weapons
        weapon = raw_input()
        for outcome in outcomes:
            if outcome["weapon"].upper() != weapon.upper():
                ret.append(outcome)
    elif typ.upper() == "S":
        print"Enter the innocent suspect (%s):" % suspects
        suspect = raw_input()
        for outcome in outcomes:
            if outcome["suspect"].upper() != suspect.upper():
                ret.append(outcome)
    return ret
    
def main(): #reruns after a new hint is entered
    outcomes = []
    print "%s outcomes left." % len(outcomes)
    while (len(outcomes) > 1):
        outcomes = input(outcomes)
        
main()

def solution(): #displays answer once the number of combinations is equal to 1
    outcomes = generateOutcome()
    print "%s did it with the %s" % suspects, weapons
    while (len(outcomes) == 1):
        outcomes = input(outcomes)
        
solution()