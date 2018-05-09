from Player import Player
from AIPlayer import AIPlayer
from Dealer import Dealer
from Card import Card
def printInstruction(gameResources):
    '''Starts game and shows welcome message and rules'''
    print('Welcome to Linger Longer!')
    print('This is a 4 person game with 1 human player and 3 AI players.')
    print('The game starts with a trump suit.')
    print('Each player is given 4 cards.')
    print('Player 1 plays a card in the beginning of the round and then')
    print('player 2 does next and so on. Player wins a round by playing')
    print('the highest value card that is a trump suit.')
    print('If no card with a trump suit is played, then the highest value')
    print('card wins. Everybody but the winner of a round draws a card at')
    print('the end of the turn.')
    print('Win the game by running out cards in your hand or by having the')
    print('least amount of cards when the deck runs out cards.')

#creates players and deals cards to the players
def setUp(gameResources):
    gameResources["players"] = []
    gameResources["players"].append(Player())
    for x in range(0,3):
        gameResources["players"].append(AIPlayer())

    gameResources["cardsinplay"] = []
    d = Dealer()
    gameResources["dealer"] = d
    d.dealHand(gameResources["players"], 4, 4)
    gameResources["currentPlayer"] = 0
    gameResources["gameOver"] = False
    gameResources["trumpsuit"] = d.dealCard().suit
    gameResources["cardsinplay"] = []

def setUpRound(gameResources):
    gameResources["round"] = 0

def incrementRound(gameResources):
    gameResources["cardsinplay"] = []
    gameResources["playerindex"] = []
    gameResources["currentPlayer"] = 0
    gameResources["roundIsNotOver"] = True
    gameResources["round"] += 1
    print()
    print('---------------------ROUND %d---------------------' % gameResources["round"])
    for i in range(1,4):
        print("AI Player %(num)d has %(cNum)d cards" % {"num": (i+1), "cNum":len(gameResources["players"][i].hand)})
    print()
    print('The trump suit is %s' % Card.SUITS[gameResources["trumpsuit"] - 1])


def playCard(gameResources):
    d = gameResources["dealer"]
    if gameResources["currentPlayer"] == 0:
        player = gameResources["players"][0]
        k = 1
        for card in player.hand:
            cardStr = Card.string(card)
            print(" %(num)d) %(card)s" % {"num": k, "card":cardStr})
            k += 1
        while True:
            try:
                print("Enter desired card position to play:")
                cardnum = int(input())
                gameResources["cardsinplay"].append(player.hand[(cardnum - 1)])
                print("You play %(card)s" % { "card":Card.string(player.hand[(cardnum - 1)])})
                del player.hand[(cardnum - 1)]
                gameResources["playerindex"].append(gameResources["currentPlayer"])
                break
            except: 
                print("Invalid number")
        if len(player.hand) <= 0:
            gameResources["emptyHand"] = True
    #the ai moves
    if gameResources["currentPlayer"] >= 1:
        if gameResources["currentPlayer"] == 3:
            gameResources["roundIsNotOver"] = False
        player = gameResources["players"][gameResources["currentPlayer"]]
        try:
            highest = player.hand[0]
            index = 0
            for i, card in enumerate(player.hand):
                if card.suit == gameResources["trumpsuit"] and (card.value > highest.value or highest.suit != gameResources["trumpsuit"]):
                    highest = card
                    index = i
                elif card.suit != gameResources["trumpsuit"]:
                    if highest.suit != gameResources["trumpsuit"] and card.value > highest.value:
                        highest = card
                        index = i
            gameResources["cardsinplay"].append(player.hand[index])
            print("AI Player %(num)d plays %(card)s" % { "num": (gameResources["currentPlayer"] + 1), "card":Card.string(player.hand[index])})
            del player.hand[index]
            gameResources["playerindex"].append(gameResources["currentPlayer"])
        except IndexError:
            print("AI Player %(num)d has no cards left to play" % { "num": (gameResources["currentPlayer"] + 1)})
        if len(player.hand) <= 0:
            gameResources["emptyHand"] = True
    gameResources["currentPlayer"] += 1
    if len(d.deck.cards) <= 4:
        gameResources["emptydeck"] = True 

def roundEnd(gameResources):
    d = gameResources["dealer"]
    highest = gameResources["cardsinplay"][0]
    index = 1
    for i, card in enumerate(gameResources["cardsinplay"]):
        if card.suit == gameResources["trumpsuit"] and (card.value > highest.value or highest.suit != gameResources["trumpsuit"]):
            highest = card
            index = i+1
        elif card.suit != gameResources["trumpsuit"]:
            if highest.suit != gameResources["trumpsuit"] and card.value > highest.value:
                highest = card
                index = i+1
        
    # index = next((i for i, card in enumerate(gameResources["cardsinplay"]) if card.suit == gameResources["trumpsuit"]), -1)
    if index !=  -1:
        # for x in range(0, len(gameResources["cardsinplay"])):
            # for y in range(0, len(gameResources["cardsinplay"])):
                # if gameResources["cardsinplay"][y].value >= gameResources["cardsinplay"][x].value:
                    # index = y
        print("Player %(num)d wins the round and all other players draw a card"% {"num": index})
        for i in range(0, 4):
            if i != (index - 1):
                gameResources["players"][i].hand.append(d.dealCard())
    else:
        print("Player %(num)d wins the round and all other players draw a card"% {"num": index})
        for i in range(0, 4):
            if i != (index - 1):
                gameResources["players"][i].hand.append(d.dealCard())


def winner(gameResources):
    if gameResources["emptydeck"] == True:
        index = 0
        handsize = 100
        for i in range(0, 4):
            if len(gameResources["players"][i].hand) <= handsize:
                index = i
        print("Player %(num)d wins the game because they have the least cards" % {"num": (i + 1)})
    else:
        for i in range(0, 4):
            if len(gameResources["players"][i].hand) <= 0:
                print("Player %(num)d has ran out of cards and won the game" % {"num": (i + 1)})



