# play bartok

from PlayerBartok import PlayerBartok
from Dealer import Dealer
from Card import Card
import PlayerBartok
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

def startGame():
    while True:
        for i in range(0, numOfPlayers):
            print()
            print("Current card on top: %s" % Card.string(discardList[0]))
            printPlayerHand(players[i])
            print("Enter desired card position to play (press -1 to draw):")
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
                return i
            if(len(d.deck.cards) <= 0):
                return -1

def main():
    print("Rules of Bartok:\n")
    loop = True
    global numOfPlayers
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
        players.append(PlayerBartok)
    #deals the cards   
    #d = Dealer()
    d.dealBartok(players)
    #initlized the discard pile
    discardList.append(d.deal1Card())
    playernum = startGame()
    if playernum <= 0:
        print("The game is a tie!")
    else:
        print("Player %d wins!" % playernum)


if  __name__ =='__main__':
    main()
