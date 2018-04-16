from Game import GameType, Answer
import FSM

def runGame():
    playAgain = 'yes'
    while playAgain == 'yes':
        correctInput = False
        while correctInput != True:
            print("------------------------------------------")
            cardGame = input("Choose the game you would like to play:\nChoices: Bartok <----> War\n").lower()
            if cardGame == 'bartok':
                correctInput = True
                print("\nBartok is starting up...\nEnjoy your game!")
                print("------------------------------------------\n")
                newGame = FSM.BartokMachine()
            elif cardGame == 'war':
                correctInput = True
                print("\nWar is starting up...\nEnjoy your game!")
                print("------------------------------------------\n")
                newGame = FSM.WarMachine()
            else:
                print("Invalid input. Please enter a valid card game.\n")
        playAgain = input("\nWould you like to play another game? (Yes/No)\n").lower()
    print("\nSystem exiting...")
    print("Thank you for playing!")
    
if  __name__ =='__main__':
    runGame()