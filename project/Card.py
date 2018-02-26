class Card:
    bool up = True
    bool down = False
    def __init__(self, value, suit, face = self.down, faceCard = False):
        self.value = value
        self.suit = suit
        self.face = face
        self.faceCard = faceCard

    def bool isFaceCard():
        if self.faceCard:
            return True
        else:
            return False
    def flip():
        if self.face:
            self.face = self.up
        else:
            self.face = self.down