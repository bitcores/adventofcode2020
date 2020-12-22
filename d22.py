import time
from collections import defaultdict
from copy import deepcopy
st = time.time()

inputfile = "input22.txt"

def readinput():
    L = defaultdict(list)
    p = 0
    with open(inputfile) as fp:
        for line in fp:
            line = line.strip()

            if "Player" in line:
                p = int(line[-2])
            if line.isdigit():
                L[p].append(int(line))
            
    return L

def splitinput():
    L = [i.split("\n") for i in open(inputfile).read().split("\n\n")]

    return L

## Parse input
inp = readinput()
#inp = splitinput()

## Solve problem
def combat(plr, deck, r):
    seen = set()
    winner = []
        
    while(True):
        if r:
            s = ""
            for y in deck:
                for x in deck[y]:
                    s += str(x)
                s += " "
            if s in seen:
                #print("game seen", s)
                winner = deepcopy(deck[1])
                return winner, plr[0]
            else:
                seen.add(s)

            #print(deck)
            #input()
        # round draw
        comp = [0,0]
        for p in plr:
            comp[p-1] = deck[p].pop(0)

        if r and comp[0] <= len(deck[1]) and comp[1] <= len(deck[2]):
            #print("subgame", comp[0], len(deck[1]), comp[1], len(deck[2]))
            subdeck = {}
            subdeck[1] = deepcopy(deck[1][:comp[0]])
            subdeck[2] = deepcopy(deck[2][:comp[1]])
            ww,pp = combat(plr, deepcopy(subdeck), r)
            if pp == plr[0]:
                deck[1].append(comp[0])
                deck[1].append(comp[1])
            else:
                deck[2].append(comp[1])
                deck[2].append(comp[0])
        else:
            if comp[0] > comp[1]:
                deck[1].append(comp[0])
                deck[1].append(comp[1])
            else:
                deck[2].append(comp[1])
                deck[2].append(comp[0])
        
        if len(deck[1]) == 0:
            winner = deepcopy(deck[2])
            return winner, plr[1]
        elif len(deck[2]) == 0:
            winner = deepcopy(deck[1])
            return winner, plr[0]

players = list(inp.keys())

winner, player = combat(players, deepcopy(inp), False)
winner.reverse()
score = 0
for r in range(0,len(winner)):
    score += winner[r] * (r+1)

print("Part 1:> ", score)

score = 0
winner, player = combat(players, deepcopy(inp), True)
winner.reverse()
score = 0
for r in range(0,len(winner)):
    score += winner[r] * (r+1)

print("Part 2:> ", score)

## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)