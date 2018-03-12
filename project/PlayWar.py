# play war
from Card import Card
from collections import deque
from Deck import Deck
from PlayerWar import PlayerWar
from Dealer import Dealer

cardList = []
tieList = []
roundNum = 0

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

    print('Player 1 plays card ' + cardP1.string())
    print('Player 2 plays card ' + cardP2.string())
    try:
        p1.hand = p1.hand[1:]
        p2.hand = p2.hand[1:]

        if cardP1.value > cardP2.value:
            cardList.append(cardP1)
            cardList.append(cardP2)
            print('Player 1 wins the round!')
            print('-----------------------------------------------------')
            return 1
        elif cardP1.value < cardP2.value:
            cardList.append(cardP2)
            cardList.append(cardP1)
            print('Player 2 wins the round!')
            print('-----------------------------------------------------')
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
    except IndexError:
        if len(p1.hand) == 0:
            return 2
        elif len(p2.hand) == 0:
            return 1

def main():
        
    '''Starts game and shows welcome message and rules'''
    print('Welcome to WAR!')
    print('Each player starts with half of a shuffled 52 card deck.')
    print('Players may not look at the cards in their hands.')
    print('Each player pulls one card from the deck and puts it on the table.')
    print('The higher card wins; the player who played it takes both cards and places them on the bottom of his stack.') 
    print('Aces are always higher than Kings in this game, but they are often lower than Jokers (if used).')
    print('A "war" occurs when the two players play the same rank (two 9s, for example), making a tie.')
    print('Each player then deals three cards facedown (the spoils are for the winner) and a face-up card.')
    print('The player with the higher face-up card takes all the cards from the war into his stack.')

    p1 = PlayerWar()
    p2 = PlayerWar()
    d = Dealer()
    global cardList
    global roundNum

    d.dealWar(p1, p2)

    hasCards = True
    while hasCards:
        roundNum = roundNum + 1
        print('---------------------ROUND %d---------------------' % roundNum)
        winner = giveCards(p1.hand[0], p2.hand[0], p1, p2)
        if winner == 1:
            for c in cardList:
                p1.hand.append(cardList.pop())
        elif winner == 2:
            for c in cardList:
                p2.hand.append(cardList.pop())
        hasCards = (len(p1.hand) != 0) and (len(p2.hand) != 0)
        
    if not p1.hand:
        print('Player 2 has won the game!')
        print('-----------------------------------------------------')
    elif not p2.hand:
        print('Player 1 has won the game!')
        print('-----------------------------------------------------')

if  __name__ =='__main__':
    main()
