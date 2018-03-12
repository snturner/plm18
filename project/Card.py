class Card:
    up = True
    down = False

    VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["SP", "C", "H", "D"]

    def __init__(self, value, suit, face = down, faceCard = False):
        self.value = value
        self.suit = suit
        self.face = face
        self.faceCard = faceCard

    def string(self):
        cardValue = self.value
        cardSuit = self.suit
        return cardValue + cardSuit

    def isFaceCard(self):
        faceList = [10, 11, 12]
        for f in faceList:
            if self.suit == f:
                return True
        return False

    def flip(self):
        if self.face == False:
            self.face = True
        else:
            self.face = False
