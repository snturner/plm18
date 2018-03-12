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

    def isFaceCard():
        if self.faceCard:
            return True
        else:
            return False
    def flip():
        if self.face:
            self.face = self.up
        else:
            self.face = self.down
