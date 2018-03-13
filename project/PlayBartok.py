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
    i = 1
    for card in player.hand:
        cardStr = Card.string(card)
        print(" %(num)d) %(card)s" % {"num": i, "card":cardStr})
        i += 1

def startGame():
    while True:
        for i in range(0, numOfPlayers):
            printPlayerHand(players[i])
            print(" press -1 to draw")
            cardnum = int(input("Pick the number of the card to play:"))
            cardPlayed = players[i].hand[(cardnum - 1)]
            if cardnum == -1:
                print("Player %(num)d draws a card"% {"num": i})
                players[i].hand.append(d.deal1Card())
            elif cardPlayed.value == discardList[0].value or cardPlayed.suit == discardList[0].suit :
                discardList.insert(0, cardPlayed)
                del players[i].hand[(cardnum - 1)]
            else:
                print("Invalid card, Player %(num)d draws a card"% {"num": i})
                players[i].hand.append(d.deal1Card())
            if(len(players[i].hand) <= 0):
                return i
            if(len(d.deck.cards) <= 0):
                return -1

def main():
    print("Rules of Bartok:\n")
    loop = True
    while loop:
        try:
            numOfPlayers = int(input("How many players are there?"))
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
    playernumm = startGame()
    if playernum <= 0:
        print("The game is a tie!")
    else:
        print("Player " + playernum + " wins")


if  __name__ =='__main__':
    main()
