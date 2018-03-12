from random import shuffle
import Card

class Deck:
    up = True
    down = False

    def __init__(self):
        Deck.makeList(self)
        random.shuffle(self)
    
    def makeList(deck):
        for x in range(0,4):
            for y in range(0, 13):
                ##y is the value, x is suit
                ## for y, 10 - 14 is J-A respectively 
                ## for x, 1 - SP, 2 - C, 3 - H, 4 - D
                deck[y + x] = Card(y + 2, x + 1, False, True)

