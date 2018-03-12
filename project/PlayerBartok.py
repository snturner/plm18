class PlayerBartok:
	Hand cardsList
	DiscardPile pile
	def __init__(self, cards, cardsList):
		self.cards = 7
	def isDraw(self, cardsList, pile):
		self.cardsList = pile.top
		while pile.next != empty?:
			pile.top = pile.next
	def turn(self, cardsList, lastCard, pile):
		...
