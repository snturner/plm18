class Transition():
    def __init__(self, guard, end):
        self.guard = guard
        self.end   = end
        self.actions = []
    
    def addactions(self, f):
        self.actions += f

class State():
    def __init__(self, onEntry=None, name):
        if onEntry is not None: onEntry()
        self.name = name
        self.transitions = []

    def addtransition(self, transition):
         self.transitions += transition

    def step(self):
        for t in self.transitions:
            if t.guards is not None:
                if(t.guard is True):
                    for action in t.actions:
                        action()
                    return t.end

    def onEntry(self): pass

    def onExit(self): pass

class FSM():  
    def __init__(self, start):
        self.states = []
        self.start = start
        self.currentstate = start

    def addState(self, state):
        self.states += state

    def run(self):
        while True:
            self.currentstate = currentstate.step()
            if state.quit():
                break

class Bartok():
     def __init__(self):
        run()
    def run():
        #states
        start = State(startGame(), "start")
        #transitions
        setupT = Transition(true, startGame)
        setUpT.addactions(setupGame)
        start.addtransition(setupT)

        #setup the fsm
        fsm = FSM(start)


