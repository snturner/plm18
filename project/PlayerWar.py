from random import shuffle
import HandWar
import Card

class PlayWar:
    Hand hand

    def Card playCard():
        Card cardToPlay = hand[0]
        hand = hand[1:]
        return cardToPlay
    