import time
from copy import deepcopy
st = time.time()


inputfile = "input11.txt"

def readinput():
    L = {}
    y = 0
    with open(inputfile) as fp:
        for line in fp:
            if y not in L:
                L[y] = {}
            line = line.strip()

            for x in range(0, len(line)):
                L[y][x] = line[x]
            y += 1
            
    return L

def splitinput():
    L = [i.split("\n") for i in open(inputfile).read().split("\n\n")]

    return L

## Parse input
inp = readinput()
#inp = splitinput()

## Solve problem
#print(inp)
part2 = True
seats = deepcopy(inp)
def cntadjseats(pos):
    #adj seats are 
    #-1,-1 -1,0 -1,+1
    #0,-1 0,+1
    #+1,-1 +1,0 +1,+1
    ocp = 0
    if not part2:
        for y in range(pos[0]-1, pos[0]+2):
            for x in range(pos[1]-1, pos[1]+2):
                if y == pos[0] and x == pos[1]:
                    continue
                if y not in seats or x not in seats[y]:
                    continue
                if seats[y][x] == "#":
                    ocp += 1
    else:
        d = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]      
        for dd in d:
            dpos = deepcopy(pos)
            while True:
                dpos[0] += dd[0]
                dpos[1] += dd[1]

                if dpos[0] not in seats or dpos[1] not in seats[dpos[0]]:
                    break
                if seats[dpos[0]][dpos[1]] == "L":
                    break
                elif seats[dpos[0]][dpos[1]] == "#":
                    ocp +=1
                    break

    return ocp

stable = False
while not stable:
    changes = 0
    seatcopy = deepcopy(seats)
    for dy in seats:
        for dx in seats[dy]:
            if seats[dy][dx] == "L":
                if cntadjseats([dy,dx]) == 0:
                    changes += 1
                    seatcopy[dy][dx] = "#"
            elif seats[dy][dx] == "#":
                if (cntadjseats([dy,dx]) >= 4 and not part2) or (cntadjseats([dy,dx]) >= 5 and part2):
                    changes += 1
                    seatcopy[dy][dx] = "L"
    
    if changes == 0:
        stable = True
    else:
        seats = deepcopy(seatcopy)
        #print(seats)
        #input()

occsum = 0
for cy in seats:
    occsum += sum(value == "#" for value in seats[cy].values())
print(occsum)

## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)