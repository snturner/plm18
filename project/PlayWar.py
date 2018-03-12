# play war
import Card
from collections import deque
import Deck
import PlayerWar
import Dealer

class PlayWar:
    Card cardList
    Card tieList

#   def giveCards(p1, p2):
#       cardList = [p1.hand[0], p2.hand[0]]
#       p1.hand = p1.hand[1:]
#       p2.hand = p2.hand[1:]
#       Card cardP2 = cardList.pop()
#       Card cardP1 = cardList.pop()
#       if cardP1.value > cardP2.value:
#           for c in cardList:
#               p1.hand = p1.hand + c
#       else if cardP1.value < cardP2.value:
#           for c in cardList:
#               p2.hand = p2.hand + c
#       else:
#           bool isWar = true
#           while isWar:
              
    def giveCards(cardP1, cardP2, p1, p2):
        global cardList
        global tieList

        p1.hand = p1.hand[1:]
        p2.hand = p2.hand[1:]

        if cardP1.value > cardP2.value:
            cardList.append(cardP1)
            cardList.append(cardP2)
            return 1
        else if cardP1.value < cardP2.value:
            cardList.append(cardP2)
            cardList.append(cardP1)
            return 2
        else:
            cardList.append(p1.hand[0])
            cardList.append(p1.hand[1])
            cardList.append(p2.hand[0])
            cardList.append(p2.hand[1])
            p1.hand = p1.hand[2:]
            p2.hand = p2.hand[2:]
            winner = giveCards(p1.hand[0], p2.hand[0], p1, p2)
            return winner

    def __main__():
        
        '''Starts game and shows welcome message and rules'''
        print 'Welcome to WAR! \nEach player starts with half of a shuffled 52 card deck.
        print 'Players may not look at the cards in their hands.' 
        print 'Each player pulls one card from the deck and puts it on the table.' 
        print 'The higher card wins; the player who played it takes both cards and places them on the bottom of his stack. 
        print 'Aces are always higher than Kings in this game, but they are often lower than Jokers (if used).'
        print 'A "war" occurs when the two players play the same rank (two 9s, for example), making a tie.' 
        print 'Each player then deals three cards facedown (the spoils are for the winner) and a face-up card.' 
        print 'The player with the higher face-up card takes all the cards from the war into his stack.'

        PlayerWar p1, p2
        Dealer d
        global cardList

        d.dealWar(p1, p2)

        bool hasCards = true
        while hasCards:
            winner = giveCards(p1.hand[0], p2.hand[0], p1, p2)
            if winner == 1:
                for c in cardList:
                    p1.hand = p1.hand + c
            else if winner == 2:
                for c in cardList:
                    p2.hand = p2.hand + c


