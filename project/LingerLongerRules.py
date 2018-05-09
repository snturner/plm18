from Player import Player
from AIPlayer import AIPlayer
from Dealer import Dealer
from Card import Card
def printInstruction(gameResources):
    '''Starts game and shows welcome message and rules'''
    print('Welcome to Linger Longer!')
    print('This is a 4 person game with 1 human player and 3 AI players')
    print('The game starts with a trump suit')
    print('Each player is given 4 cards')
    print("Player 1 plays a card in the beginning of the round and then player 2 and so forth")
    print('Player wins a round by playing the higest value card that is a trump suit')
    print('If no card with a trump suit is played, then the highest value card wins')
    print("Everybody but the winner of a round draws a card at the end of the turn")
    print("Win the game by running out cards in your hand or by having the least amount of cards when the deck runs out cards")

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
    print('---------------------ROUND %d---------------------' % gameResources["round"])
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
                print("Enter desired card position to play (enter -1 to draw):")
                cardnum = int(input())
                if cardnum == -1:
                    print("Player %(num)d draws a card"% {"num": (gameResources["currentPlayer"] + 1)})
                    player.hand.append(d.dealCard())
                else:
                    gameResources["cardsinplay"].append(player.hand[(cardnum - 1)])
                    print("You play %(card)s" % { "card":Card.string(player.hand[(cardnum - 1)])})
                    player.hand.pop(cardnum - 1)
                    gameResources["playerindex"].append(gameResources["currentPlayer"])
                break
            except: 
                print("Invalid number")
    #the ai moves
    if gameResources["currentPlayer"] >= 1:
        if gameResources["currentPlayer"] == 3:
            gameResources["roundIsNotOver"] = False
        player = gameResources["players"][gameResources["currentPlayer"]]
        index = next((i for i, card in enumerate(player.hand) if card.suit == gameResources["trumpsuit"]), -1)
        if index == -1:
            for x in range(0, len(gameResources["cardsinplay"])):
                for y in range(0, len(player.hand)):
                    if player.hand[y].value >= gameResources["cardsinplay"][x].value:
                        index = y

        if index == -1:
            print("AI Player %(num)d draws a card"% {"num": (gameResources["currentPlayer"] + 1)})
            player.hand.append(d.dealCard())
        else:
            gameResources["cardsinplay"].append(player.hand[index])
            print("AI Player %(num)d plays %(card)s" % { "num": (gameResources["currentPlayer"] + 1), "card":Card.string(player.hand[index])})
            player.hand.pop(index)
            gameResources["playerindex"].append(gameResources["currentPlayer"])
    gameResources["currentPlayer"] += 1
    for i in range(0, 4):
        if len(gameResources["players"][i].hand) <= 0:
            gameResources["emptyHand"] = True
    if len(d.deck.cards) <= 4:
        gameResources["emptydeck"] = True 

def roundEnd(gameResources):
    d = gameResources["dealer"]
    index = next((i for i, card in enumerate(gameResources["cardsinplay"]) if card.suit == gameResources["trumpsuit"]), -1)
    if not index ==  -1:
        for x in range(0, len(gameResources["cardsinplay"])):
            for y in range(0, len(gameResources["cardsinplay"])):
                if gameResources["cardsinplay"][y].value >= gameResources["cardsinplay"][x].value:
                    index = y
        print("Player %(num)d wins the round and all other players draw a card"% {"num": gameResources["playerindex"][index]})
        for i in range(0, 4):
            if not i == index:
                gameResources["players"][i].hand.append(d.dealCard())
    else:
        print("Player %(num)d wins the round and all other players draw a card"% {"num": gameResources["playerindex"][index]})
        for i in range(0, 4):
            if not i == index:
                gameResources["players"][i].hand.append(d.dealCard())


def winner(gameResources):
    if gameResources["emptydeck"] == True:
        index = 0
        handsize = 100
        for i in range(0, 4):
            if len(gameResources["players"][i].hand) <= handsize:
                index = i
        print("Player %(num)d wins the game because they have the least cards" % {"num": i})
    else:
        for i in range(0, 4):
            if len(gameResources["players"][i].hand) <= 0:
                print("Player %(num)d has ran out of cards and won the game" % {"num": i})



