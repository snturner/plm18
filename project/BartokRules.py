import sys
from Player import Player
from Dealer import Dealer
from Card import Card
def printInstruction(gameResources):
    '''Starts game and shows welcome message and rules'''
    print("Rules of Bartok:\n")
    print("There must be at least 2 players and at most 6 players.")
    print("Players play turn-based rounds where one player")
    print("plays a card from their hand only if that card matches either the")
    print("value or the suit of the faced-up card and draws a card from ")
    print("the deck if the player has no matches. Then the next player has a turn.")
    print("The game is won by the player who has no cards left in their hand.\n")

#creates players and deals cards to the players
def setUp(gameResources):
    gameResources["players"] = []
    loop = True
    while loop:
        try:
            print("Enter number of players (2 - 6):")
            numOfPlayers = int(input())
            if numOfPlayers < 2 or numOfPlayers >= 7:
                print("There must be between 2 - 6 players")
            else:
                loop = False
        except:
            print("Invalid number")
    gameResources["numPlayers"] = numOfPlayers
    for i in range(0, numOfPlayers):
        gameResources["players"].append(Player())
    gameResources["currentPlayer"] = 0
    d = Dealer()
    d.dealHand(gameResources["players"], numOfPlayers, 6)
    gameResources["dealer"] = d
    gameResources["discardList"] = []
    gameResources["discardList"].append(d.dealCard())
    gameResources["gameOver"] = False
    
def setUpRound(gameResources):
    gameResources["round"] = 0
    
def incrementRound(gameResources):
    gameResources["round"] += 1
    print('---------------------ROUND %d---------------------' % gameResources["round"])

# prints out the player's start of turn
def printPlayerHand(gameResources):
    playerNum = gameResources["currentPlayer"]
    player = gameResources["players"][playerNum]
    print("---------------------PLAYER %d's TURN---------------------" % (playerNum + 1))
    print("Current card on top: %s" % Card.string(gameResources["discardList"][0]))
    k = 1
    for card in player.hand:
        cardStr = Card.string(card)
        print(" %(num)d) %(card)s" % {"num": k, "card":cardStr})
        k += 1

# player selects card through command line
def playerPicksCard(gameResources):
    d = gameResources["dealer"]
    playerNum = gameResources["currentPlayer"]
    player = gameResources["players"][playerNum]
    while True:
        try:
            print("Enter desired card position to play (enter -1 to draw):")
            cardnum = int(input())
            if cardnum == -1:
                print("Player %(num)d draws a card"% {"num": (playerNum + 1)})
                player.hand.append(d.dealCard())
            else:
                gameResources["cardpicked"] = player.hand[(cardnum - 1)]
            gameResources["cardnum"] = cardnum
            break
        except: 
            print("Invalid number")

# player card is played
def playCard(gameResources):
    d = gameResources["dealer"]
    playerNum = gameResources["currentPlayer"]
    player = gameResources["players"][playerNum]
    cardnum = gameResources["cardnum"] 
    if cardnum != -1:
        cardToPlay = gameResources["cardpicked"]
        if Card.compare(cardToPlay.value, gameResources["discardList"][0].value) == 0 or Card.compare(cardToPlay.suit, gameResources["discardList"][0].suit) == 0:
            gameResources["discardList"].insert(0, cardToPlay)
            del player.hand[(cardnum - 1)]
        else:
            print("Invalid card, Player %(num)d draws a card"% {"num": (playerNum + 1)})
            player.hand.append(d.dealCard())

# swaps to next player
def nextPlayer(gameResources):
    playerNum = gameResources["currentPlayer"]
    if playerNum == (gameResources["numPlayers"] - 1):
        gameResources["currentPlayer"] = 0
        gameResources["nextround"] = True
    else:
        gameResources["nextround"] = False
        gameResources["currentPlayer"] += 1

# end of game is determined
def winner(gameResources):
    players = gameResources["players"]
    numPlayers = gameResources["numPlayers"]
    for i in range(0, numPlayers):
        if len(players[i].hand) == 0:
            gameResources["hasCards"] = False
    gameResources["emptyHand"] = not gameResources["hasCards"]

# winner is printed
def printWinner(gameResources):
    d = gameResources["dealer"]
    players = gameResources["players"]
    numPlayers = gameResources["numPlayers"]
    for i in range(0, numPlayers):
        if(len(d.deck.cards) <= 0):
            print("The game is a tie!")
            break
        if(len(players[i].hand) <= 0):
            print("Player %d wins!" %  (i + 1))
            break
        
    
    
    
