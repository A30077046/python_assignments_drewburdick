rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

def buildDeck(rank, suit):
    deck= []
    for s in suit:
        for r in rank:
            deck.append("%s of %s" % (r,s))
    return deck
    
def shuffle(deck):
    one = []
    two = []
    one = deck[0:len(deck)/2]
    two = deck[len(deck)/2:]
    mixedUp = []
    for h in range(0, len(deck)):
        if h % 2 == 0:
            mixedUp.append(one[0])
            del one[0]
    return mixedUp
    
def deal(deck):
    return deck[0:5]

def main():
    buildDeck(rank, suit)
    print "How many times do you want to shuffle the deck?",
    userInput = int(raw_input())
    for h in range(0,userInput):
        s = shuffle(buildDeck(rank, suit))
    print deal(buildDeck(rank, suit))

main()


