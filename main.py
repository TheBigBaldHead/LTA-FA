from FA import NFA, State, Transition

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
