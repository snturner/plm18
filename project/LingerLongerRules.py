from Player import Player
from Dealer import Dealer
from Card import Card
def printInstruction(gameResources):
    '''Starts game and shows welcome message and rules'''
    print("Rules of Linger Longer:\n")
    print("There must be at least 4 players to play the game. The")
    print("game starts with the dealer dealing out cards as many")
    print("as there are players. Then the dealer takes a card from")
    print("the remaining deck to use as a \"trump\" card for the")
    print("game. Gameplay begins, and each player either plays a")
    print("card with the same suit of the trump card or any other")
    print("card in their hand. In each round, play continues until")
    print("all players have played a card. Then the player with the")
    print("highest card wins the highest card played. That player")
    print("puts out a card first during the next round.")
    print("The game is won by the player who is the last to have")
    print("cards in their hand.")