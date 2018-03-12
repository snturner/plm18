# play bartok

import Dealer
import PlayerBartok

#number of players
numOfPlayers
#Creates players
PlayerBartok players
#creates the discard pile
Card discardList
#deals the cards
d = Dealer()
def int startGame:
    while true:
        for i in range(0, numOfPlayers):
            cardnum = int(raw_inpu("Pick the number of the card to play:"))
            players[i].printHand()
            print(" press -1 to draw")
            cardPlayed = player[i].hand[(cardnum - 1)]
            if cardnum = -1:
                print("Draw a card")
                players[i].hand.append(d.deal1Card())
            else if cardPlayed.value == discardList[0].value or cardPlayed.suit == discardList[0].suit :
                discardList.insert(0, cardPlayed)
                del player[i].hand[(cardnum - 1)]
            else:
                print("Invalid card, draw a card")
                players[i].hand.append(d.deal1Card())
            if(len(player[i].hand) <= 0):
                return i
            if(len(d.deck) <= 0):
                return -1

def main():
    print("Rules of Bartok:\n")
    loop = True
    while loop:
        try:
            numOfPlayers = int(raw_input("How many players are there?"))
            if pnumOfPlayers < 2 and numOfPlayers < 7
                print("There must be between 2 - 6 players")
            else:
                loop = False
        except:
            print("Enter a valid number")

    for i in range(0, players):
        players[i] = PlayerBartok()

    d.dealPlayers(players)
    #initlized the discard pile
    discardList = d.deal1Card()
    playernumm = startGame()
    if playernum <=0 0:
        print("The game is a tie!")
    else:
        print("Player " + playernum + " wins")


if  __name__ =='__main__':
    main()
