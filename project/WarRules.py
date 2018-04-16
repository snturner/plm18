from Player import Player
from Dealer import Dealer
from Card import Card
def printInstruction(gameResources):
    '''Starts game and shows welcome message and rules'''
    print('Welcome to WAR!')
    print('Each player starts with half of a shuffled 52 card deck.')
    print('Players may not look at the cards in their hands.')
    print('Each player pulls one card from the deck and puts it on the table.')
    print('The higher card wins; the player who played it takes both cards and places them on the bottom of his stack.') 
    print('Aces are always higher than Kings in this game, but they are often lower than Jokers (if used).')
    print('A "war" occurs when the two players play the same rank (two 9s, for example), making a tie.')
    print('Each player then deals three cards facedown (the spoils are for the winner) and a face-up card.')
    print('The player with the higher face-up card takes all the cards from the war into his stack.')

#creates players and deals cards to the players
def setUp(gameResources):
    gameResources["players"] = []
    gameResources["players"].append(Player())
    gameResources["players"].append(Player())
    gameResources["cardsinplay"] = []
    d = Dealer()
    d.dealHand(gameResources["players"], 2, 26)

def setUpRound(gameResources):
    gameResources["round"] = 0

def incrementRound(gameResources):
    gameResources["round"] += 1
    print('---------------------ROUND %d---------------------' % gameResources["round"])

def player1PlaysCard(gameResources):
    p1 = gameResources["players"][0]
    gameResources["cardsinplay"].insert(0, p1.hand[0])
    p1.hand = p1.hand[1:]


def player2PlaysCard(gameResources):
    p2 = gameResources["players"][1]
    gameResources["cardsinplay"].insert(1, p2.hand[0])
    p2.hand = p2.hand[1:]

def winner(gameResources):
    p1 = gameResources["players"][0]
    p2 = gameResources["players"][1]
    p1card = gameResources["cardsinplay"][0]
    p2card = gameResources["cardsinplay"][1]
    print('Player 1 plays card ' + p1card.string())
    print('Player 2 plays card ' + p2card.string())
    #compare the two cards
    try:
        if Card.compare(p1card.value, p2card.value) == 1:
            print('Player 1 wins the round!')
            print('-----------------------------------------------------')
            for c in gameResources["cardsinplay"]:
                p1.hand.append(gameResources["cardsinplay"].pop())
            gameResources["isTie"] = False
        elif Card.compare(p1card.value, p2card.value) == 2:
            print('Player 2 wins the round!')
            print('-----------------------------------------------------')
            for c in gameResources["cardsinplay"]:
                p2.hand.append(gameResources["cardsinplay"].pop())
            gameResources["isTie"] = False
        else:
            print('Both players tied!')
            gameResources["cardsinplay"].append(p1.hand[0])
            gameResources["cardsinplay"].append(p1.hand[1])
            gameResources["cardsinplay"].append(p2.hand[0])
            gameResources["cardsinplay"].append(p2.hand[1])
            p1.hand = p1.hand[2:]
            p2.hand = p2.hand[2:]
            gameResources["isTie"] = True

        gameResources["hasCards"]  = (len(p1.hand) != 0) and (len(p2.hand) != 0)
        gameResources["emptyHand"] = not gameResources["hasCards"]
        #print(len(p1.hand))
        #print(len(p2.hand))
        #print(gameResources["hasCards"])
        #print(gameResources["emptyHand"])
        
    except IndexError:
        if len(p1.hand) == 0 or len(p2.hand) == 0 :
            gameResources["emptyHand"] = True
            gameResources["hasCards"] = False
            gameResources["isTie"] = False

def printWinner(gameResources):
    p1 = gameResources["players"][0]
    p2 = gameResources["players"][1]
    if not p1.hand:
        print('Player 1 has run out of cards!')
        print('Player 2 has won the game!')
    elif not p2.hand:
        print('Player 2 has run out of cards!')
        print('Player 1 has won the game!')


