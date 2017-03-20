dictionary = ['bird','dog', 'snake', 'fish', 'cat', 'mouse', 'starfish', 'woodchuck', 'crab']
    #Dictionary of words that will be shuffled and matched

def userInt(prompt):
    print prompt,
    num = int(raw_input())
    return num
    #Place holder for user defined info

import random
    #Generates random order

def main():
    attempt = 0
    random.shuffle(dictionary)
    dictionary.append(dictionary[0])
    random.shuffle(dictionary)
    tryagain = True
    #Generate game/shuffle "cards"
    
    while tryagain:
        card1 = -1
        card2 = -1
    #Cards are equal to unused variables until player defines variable
        
        while options(card1, card2) == False:
            card1 = userInt("Flip Card 1 (0-9):")
            card2 = userInt("Flip Card 2 (0-9):")
    #User defines a raw input see def userInt above
            
            if options(card1, card2) == False:
                print "Invalid options, Try Again! Picking exclusively from (0-9)"
        print "Card %s is a %s." % (card1, dictionary[card1])
        print "Card %s is a %s." % (card2, dictionary[card2])
        attempt = attempt + 1
    #If userInt is false then they either don't match are don't fall within the guidelines 
        
        if (dictionary[card1] == dictionary[card2]):
            print "You won! It took you %s tries." % attempt
            tryagain = False
    #Compares user inputs to matching dictionary. Game is won if these match.
    
def options(c1,c2):
    if (c1 != c2) and (c1 >= 0 and c1 <= 9 and c2 >= 0 and c2 <= 9):
        return True
    else: 
        return False
    #Possible Outcomes

main() 