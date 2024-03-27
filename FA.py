class FA:
    def __init__(self, Language: list = list(), States: dict = dict()):
        self.initState = None
        self.States = States
        self.Language = Language + ['$']
    
    def addState(self, State):
        if self.initState == None:
            self.initState = State
        self.States[State.Name] = State

    def finalizeStates(self, finalStates):
        for State in finalStates:
            self.States[State].Final = True

    def __str__(self):
        out = "States:\n"
        for index, State in enumerate(self.States.values()):
            out += f"\t{index + 1}. {str(State)}\n"
        out += f"Language:\n\t{', '.join(self.Language)}"
        return out
    
    def checkGrammer(self, test: str, currState, index: int = 0) -> bool:
        
        if currState.Final and index == len(test): # out 
            # print(f"{currState.Name}")
            return True
        if index >= len(test):
            # print("|")
            # print("reached end of string, no result\n-------------------------")
            return False
        # print(f"{currState.Name} -> ", end="")
        # print(f"\n-------------------------------\ncheckGrammer letter {test[index]} state {currState.Name}\n-------------------------------")
        if currState.Transitions:
            # print(f"\nTransitions of state {currState.Name}")
            # print(currState.Transitions[0])
            for Transition in currState.Transitions:
                if Transition.alphabet == '$':
                    if self.checkGrammer(test, Transition.toState, index):
                        return True
                # print(test[index], [transition.alphabet for transition in currState.Transitions])
                if test[index] in [transition.alphabet for transition in currState.Transitions]:
                    if Transition.alphabet == test[index]:
                        if self.checkGrammer(test, Transition.toState, index + 1):
                            return True
                else:
                    return False

        # print("no more transitions")
        return False

class NFA(FA):
    pass

class DFA(FA):
    pass

class State:
    def __init__(self, Name: str, Final: bool = False):
        self.Name = Name
        self.Final = Final
        self.Transitions = list()
        
    def addTransition(self, alphabet: str, State):
        transition = Transition(alphabet, State)
        self.Transitions.append(transition)

    def __str__(self):
        return f'{"Final " if self.Final else ""}State {self.Name} with {"Transitions: " + ", ".join([f"({transition.alphabet},{transition.toState.Name})" for transition in self.Transitions]) if len(self.Transitions) else "no transitions"}'

class Transition:
    def __init__(self, alphabet: str, State): 
        self.toState = State
        self.alphabet = alphabet

    def __str__(self):
        return f'({self.alphabet},{self.toState.Name})'
        # return f'Transition with alphabet {self.alphabet} to State {self.toState.Name}'

if __name__ == '__main__':
    pass
    # statesName = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5']
    # Language = ['a', 'b']
    # FinalStates = ['q2', 'q5']
    # Transitions = ["q0,a,q1", 'q0,b,q4', 'q1,a,q1', 'q1,b,q2', 'q2,b,q2', 'q2,a,q3', 'q3,b,q5', 'q4,a,q5', 'q4,b,q4', 'q5,a,q5']
    # test = "bbbbbbaaa"
    # nfa = NFA(Language)
    # for letter in statesName:
    #     nfa.addState(State(letter))
    # nfa.finalizeStates(FinalStates)
    # tCount = len(Transitions)
    # for i in range(tCount):
    #     fromState, alphabet, toState = Transitions[i].split(',')
    #     nfa.States[fromState].addTransition(alphabet, nfa.States[toState])
    # print(nfa)
    # if nfa.checkGrammer(test, nfa.initState): print("Accepted")
    # else: print("Rejected")
    # print("-------")

    # input quera

    sCount = int(input())
    statesName = input().split()
    lCount = int(input())
    Language = input().split()
    nfa = NFA(Language)
    for letter in statesName:
        nfa.addState(State(letter))
    finalCount = int(input())
    FinalStates = input().split()
    nfa.finalizeStates(FinalStates)
    tCount = int(input())
    for _ in range(tCount):
        fromState, alphabet, toState = input().split(',')
        nfa.States[fromState].addTransition(alphabet, nfa.States[toState])
    test = input()
    if nfa.checkGrammer(test, nfa.initState): print("Accepted")
    else: print("Rejected")