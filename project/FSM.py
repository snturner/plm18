from War import *
from Player import Player
from Dealer import Dealer
class Transition():
    def __init__(self, guard, end):
        self.guard = guard
        self.end   = end
        self.actions = []
    
    def addactions(self, f):
        self.actions.append(f)

class State():
    def __init__(self, name, gameResources, onEntry=None):
        if onEntry is not None: onEntry()
        self.gameResources = gameResources
        self.name = name
        self.transitions = []

    def addtransition(self, transition):
         self.transitions.append(transition)
         #transition.actions[0]()

    def step(self):
        for t in self.transitions:
            if t.guard is not None:
                if(t.guard is True):
                    for action in t.actions:
                        action(gameResources)
                    return t.end

    def onEntry(self): pass


class Start(State): pass

class End(State):
    def quit(self):
        return True

class FSM():  
    def __init__(self, start):
        self.states = []
        self.start = start
        self.currentstate = start
        self.run()

    def addState(self, state):
        self.states += state

    def run(self):
        while True:
            self.currentstate = self.currentstate.step()
            if isinstance(self.currentstate, End):
                break

class WarM():
    def __init__(self):
        self.gameResources = {}
        self.gameResources["players"] = []
        self.run()

    def run(self): 
        #states
        start = Start("start", self.gameResources)
        end = End("end", self.gameResources)
        #roundBegin = State(None, "begin round")
        #playerTurn = 
        #roundEnd = 
        #win =
        #endGame =
        
        #transitions
        #start transitions
        setupT = Transition(True, end)
        setupT.addactions(setUp)
        start.addtransition(setupT)

        #setup the fsm
        fsm = FSM(start)

    #creates players and deals cards to the players
    def setUp(gameResources):
        print("h1")
        gameResources["players"].append(Player())
        gameResources["players"].append(Player())
        d = Dealer()
        print("h2")
        

if  __name__ =='__main__':
    war = WarM()
    try:
        war = WarM()
    except:
        print("\n\nGame Ended unexpectedly.\n")
        #Logger.close()
        exit()
