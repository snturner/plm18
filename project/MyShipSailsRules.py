from Player import Player
from Dealer import Dealer
from Card import Card
def printInstruction(gameResources):
    '''Starts game and shows welcome message and rules'''
    print("Rules of My Ship Sails:\n")
    print("There must be at least 4 players and at most 7 players.")
    print("Players receive 7 cards from the dealer to start. The")
    print("rest of the deck is then discarded. 
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
    loop = True
    while loop:
        try:
            print("Enter number of players (4 - 7):")
            numOfPlayers = int(input())
            if numOfPlayers < 4 or numOfPlayers >= 8:
                print("There must be between 4 - 7 players")
            else:
                loop = False
        except:
            print("Invalid number")
    gameResources["numPlayers"] = numOfPlayers
    for i in range(0, numOfPlayers):
        gameResources["players"].append(Player())
    gameResources["currentPlayer"] = 0
    d = Dealer()
    d.dealHand(gameResources["players"], numOfPlayers, numOfPlayers)
    gameResources["gameOver"] = False
    gameResources["start"] = True

# prints out the player's start of turn
def printPlayerHand(gameResources):
    playerNum = gameResources["currentPlayer"]
    player = gameResources["players"][playerNum]
    # If player is not first player of game, adds card from other player
    if not gameResources["start"]:
        player.hand.append(gameResources["prevCard"])
    # Prints hand
    print("---------------------PLAYER %d's TURN---------------------" % (playerNum + 1))
    k = 1
    for card in player.hand:
        cardStr = Card.string(card)
        print(" %(num)d) %(card)s" % {"num": k, "card":cardStr})
        k += 1

# player selects card to give through command line
def playerPicksCard(gameResources):
    playerNum = gameResources["currentPlayer"]
    player = gameResources["players"][playerNum]
    cardCount = gameResources["numPlayers"]
    while True:
        try:
            print("Enter desired card position to give away:")
            cardnum = int(input())
            if cardnum > 0 and cardnum <= cardCount:
                gameResources["prevCard"] = player.hand[(cardnum - 1)]
                gameResources["start"] = False
                del player.hand[(cardnum - 1)]
            gameResources["cardnum"] = cardnum
            break
        except: 
            print("Invalid number")

def checkHand(gameResources):
    playerNum = gameResources["currentPlayer"]
    player = gameResources["players"][playerNum]
    cardCount = gameResources["numPlayers"]
    for i in range(1, cardCount):
        if Card.compare(player.hand[i].suit, player.hand[i - 1].suit) == 0 and i == (cardCount - 1):
            gameResources["hasSuit"] = True

# swaps to next player
def nextPlayer(gameResources):
    playerNum = gameResources["currentPlayer"]
    if playerNum == (gameResources["numPlayers"] - 1):
        gameResources["currentPlayer"] = 0
    else:
        gameResources["currentPlayer"] += 1

# end of game is determined
def winner(gameResources):
    playerNum = gameResources["currentPlayer"]
    print("Player %d wins!" % (playerNum + 1))