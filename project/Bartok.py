# play bartok

from PlayerBartok import PlayerBartok
from Dealer import Dealer
from Card import Card
from PlayerBartok import PlayerBartok
from Deck import Deck
#number of players
numOfPlayers = 4
#Creates players
players = []
#creates the discard pile
discardList = []
#dealer
d = Dealer()

def printPlayerHand(player):
    k = 1
    for card in player.hand:
        cardStr = Card.string(card)
        print(" %(num)d) %(card)s" % {"num": k, "card":cardStr})
        k += 1

def startGame(players):
    while True:
        for i in range(0, numOfPlayers):
            print()
            print("----------------------PLAYER %d's TURN----------------------" % (i + 1))
            print("Current card on top: %s" % Card.string(discardList[0]))
            printPlayerHand(players[i])
            print("Enter desired card position to play (enter -1 to draw):")
            cardnum = int(input())
            if cardnum == -1:
                print("Player %(num)d draws a card"% {"num": (i + 1)})
                players[i].hand.append(d.deal1Card())
            else:
                cardPlayed = players[i].hand[(cardnum - 1)]
                if cardPlayed.value == discardList[0].value or cardPlayed.suit == discardList[0].suit:
                    discardList.insert(0, cardPlayed)
                    del players[i].hand[(cardnum - 1)]
                else:
                    print("Invalid card, Player %(num)d draws a card"% {"num": (i + 1)})
                    players[i].hand.append(d.deal1Card())
            if(len(players[i].hand) <= 0):
                return (i + 1)
            if(len(d.deck.cards) <= 0):
                return -1

def PlayBartok():
    print("Rules of Bartok:\n")
    print("There must be at least 2 players and at most 6 players.")
    print("Players play turn-based rounds where one player")
    print("plays a card from their hand only if that card matches either the")
    print("value or the suit of the faced-up card and draws a card from ")
    print("the deck if the player has no matches. Then the next player has a turn.")
    print("The game is won by the player who has no cards left in their hand.\n")
    loop = True
    global numOfPlayers
    global players
    while loop:
        try:
            print("Enter number of players (2 - 6):")
            numOfPlayers = int(input())
            if numOfPlayers < 2 or numOfPlayers >= 7:
                print("There must be between 2 - 6 players")
            else:
                loop = False
        except:
            print("Enter a valid number")

    for i in range(0, numOfPlayers):
        players.append(PlayerBartok())
    #deals the cards   
    #d = Dealer()
    d.dealBartok(players, numOfPlayers)
    #initlized the discard pile
    discardList.append(d.deal1Card())
    playernum = startGame(players)
    if playernum <= 0:
        print("The game is a tie!")
    else:
        print("Player %d wins!" % playernum)
