class Card:
    up = True
    down = False

    VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "JACK", "QUEEN", "KING", "ACE"]
    SUITS = ["SPADES", "CLUBS", "HEARTS", "DIAMONDS"]

    def __init__(self, value, suit, face = down, faceCard = False):
        self.value = value
        self.suit = suit
        self.face = face
        self.faceCard = faceCard

    def string(self):
        cardValue = ""
        cardSuit = ""
        if self.suit == 1:
            cardSuit = Card.SUITS[0]
            for c in range(1,14):
                if self.value == c:
                    cardValue = Card.VALUES[c - 1]
        elif self.suit == 2:
            cardSuit = Card.SUITS[1]
            for c in range(1,14):
                if self.value == c:
                    cardValue = Card.VALUES[c - 1]
        elif self.suit == 3:
            cardSuit = Card.SUITS[2]
            for c in range(1,14):
                if self.value == c:
                    cardValue = Card.VALUES[c - 1]
        elif self.suit == 4:
            cardSuit = Card.SUITS[3]
            for c in range(1,14):
                if self.value == c:
                    cardValue = Card.VALUES[c - 1]
        return cardValue + ' of ' + cardSuit 

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
