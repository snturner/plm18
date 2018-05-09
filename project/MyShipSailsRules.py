from Player import Player
from AIPlayer import AIPlayer
from Dealer import Dealer
from Card import Card
def printInstruction(gameResources):
    '''Starts game and shows welcome message and rules'''
    print("Rules of My Ship Sails:\n")
    print("There is one player and three AI players.")
    print("Players receive 7 cards from the dealer to start. The")
    print("rest of the deck is then discarded.")
    print("The goal of the game is to be the first player to have")
    print("a hand with seven cards all of the same suit.")
    print("Gameplay begins with the first player giving a card of")
    print("their choosing to the next player. Then the next player")
    print("gives an unwanted card to the next player, and so on.")
    print("The game is won by the player who has seven cards all")
    print("with the same suit.")

#creates players and deals cards to the players
def setUp(gameResources):
    gameResources["players"] = []
    gameResources["cardCount"] = 7
    gameResources["players"].append(Player())          # player
    gameResources["start"] = True
    for i in range(0, 3):
        gameResources["players"].append(AIPlayer())    # AI
    d = Dealer()
    d.dealHand(gameResources["players"], 4, gameResources["cardCount"])

# sets up round in game resources
def setUpRound(gameResources):
    gameResources["round"] = 0

# increments round
def incrementRound(gameResources):
    gameResources["currentPlayer"] = 0
    gameResources["turnIsNotOver"] = True
    gameResources["roundIsNotOver"] = True
    gameResources["round"] += 1
    if gameResources["round"] > 1:
            gameResources["start"] = False
            cardStr = Card.string(gameResources["prevCard"])
            print("Player 4 gave you a %(card)s." % {"card":cardStr})
    print('---------------------ROUND %d---------------------' % gameResources["round"])

# prints out the player's start of turn
def printPlayerHand(gameResources):
    playerNum = gameResources["currentPlayer"]
    player = gameResources["players"][playerNum]
    # If player is not first player of first round, adds card from other player
    if not gameResources["start"]:
        player.hand.append(gameResources["prevCard"])
    # Prints hand if first player
    if playerNum == 0:
        print("---------------------PLAYER 1's TURN---------------------")
        k = 1
        for card in player.hand:
            cardStr = Card.string(card)
            print(" %(num)d) %(card)s" % {"num": k, "card":cardStr})
            k += 1

# checks the hand for having all suits the same
def checkHand(gameResources):
    playerNum = gameResources["currentPlayer"]
    player = gameResources["players"][playerNum]
    cardCount = gameResources["cardCount"]
    gameResources["hasSuit"] = True
    for i in range(1, cardCount):
        if Card.compare(player.hand[i].suit, player.hand[i - 1].suit) != 0:
            gameResources["hasSuit"] = False
    if gameResources["hasSuit"]:
        gameResources["gameOver"] = True

# player selects card to give through command line
def playerPicksCard(gameResources):
    playerNum = gameResources["currentPlayer"]
    player = gameResources["players"][playerNum]
    cardCount = gameResources["cardCount"]
    # If player is not AI
    if playerNum == 0:
        while True:
            try:
                print("Enter desired card position to give away:")
                cardnum = int(input())
                if cardnum > 0 and cardnum <= cardCount + 1:
                    gameResources["prevCard"] = player.hand[(cardnum - 1)]
                    gameResources["start"] = False
                    del player.hand[(cardnum - 1)]
                # Saves the played card position
                gameResources["cardnum"] = cardnum
                break
            except: 
                print("Invalid number")     
    # AI turn
    else:
        cardPickedSuit = cardSuits(player.hand)
        for i in range(0, cardCount):
            if player.hand[i].suit == cardPickedSuit:
                # cardStr = Card.string(player.hand[i])
                # print("%(cp)d: %(ca)s" % {"cp":cardPickedSuit, "ca":cardStr})
                gameResources["prevCard"] = player.hand[i]
                del player.hand[i]
                # Saves the played card position
                gameResources["cardnum"] = i
                break
        # Changes back to start of round if player is 4
        if playerNum == 3:
            gameResources["roundIsNotOver"] = False
            print()
    # Turn is now over
    gameResources["turnIsNotOver"] = False



# Determines which card the AI will choose to pass on
# Not used by FSM 
def cardSuits(cards):
    spades = 0
    clubs = 0
    hearts = 0
    diamonds = 0
    for x in cards:
        if x.suit == 1:
            spades += 1
        elif x.suit == 2:
            clubs += 1
        elif x.suit == 3:
            hearts += 1
        elif x.suit == 4:
            diamonds += 1
    return lowestCard([spades, clubs, hearts, diamonds])

# Determines lowest amount of cards with suits
# Not used by FSM
def lowestCard( list ):
    min = 0
    suit = 1
    for x in range(0,4):
        if (list[suit - 1] == 0):
            suit = suit + 1
        if (list[x] < min or list[x] == min) and list[x] != 0 and list[x-1] != 0:
            min = list[x]
            suit = (x + 1)
    return suit

# swaps to next player
def nextPlayer(gameResources):
    playerNum = gameResources["currentPlayer"]
    currPlayer = playerNum + 1
    nextPlayer = playerNum + 2
    if nextPlayer <= 4:
        print("Player %(curr)d gave player %(next)d a card." % {"curr":currPlayer, "next":nextPlayer})
    gameResources["currentPlayer"] += 1
    gameResources["turnIsNotOver"] = True

# end of game is determined
def winner(gameResources):
    playerNum = gameResources["currentPlayer"]
    if playerNum != 0:
        print("\n------------------------GAME OVER------------------------")
        print("---------------------PLAYER %d's HAND---------------------" % (playerNum+1))
        player = gameResources["players"][playerNum]
        k = 1
        for card in player.hand:
            cardStr = Card.string(card)
            print(" %(num)d) %(card)s" % {"num": k, "card":cardStr})
            k += 1
    print("Player %d wins!" % (playerNum + 1))