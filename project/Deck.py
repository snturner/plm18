from random import shuffle
from Card import Card

class Deck:
    up = True
    down = False

    def __init__(self):
        self.cards = []
        Deck.makeList(self)
        shuffle(self)
    
    def makeList(self):
        for x in range(0,4):
            for y in range(0, 13):
                ##y is the value, x is suit
                ## for y, 10 - 14 is J-A respectively 
                ## for x, 1 - SP, 2 - C, 3 - H, 4 - D
                faceCard = Card(y + 2, x + 1, False, False).isFaceCard()
                self.cards.insert(y + x, Card(y + 2, x + 1, False, faceCard))

