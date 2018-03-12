from random import shuffle
class Deck:

    Card decklist
    bool up = True
    bool down = False

    def __init__(self, decklist):
        makeList()
        random.shuffle(decklist)
    
    def makeList():
        for x in range(0,4):
            for y in range(0, 13):
                ##y is the value, x is suit
                ## for y, 1 - A, 10 - 14 is J-K respectively 
                ## for x, 1 - SP, 2 - C, 3 - H, 4 - D
                decklist[y + x] = Card(y + 1, x + 1, self.down, True)
