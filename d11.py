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
def boundscheck(seats, cpos):
    return cpos[0] not in seats or cpos[1] not in seats[cpos[0]]

def cntadjseats(seats, pos, part2):
    ocp = 0
    d = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]   
    if not part2:
        for dd in d:
            y = pos[0] + dd[0]
            x = pos[1] + dd[1]

            if boundscheck(seats, [y,x]):
                continue
            if seats[y][x] == "#":
                ocp += 1
    else:           
        for dd in d:
            dpos = deepcopy(pos)
            while True:
                dpos[0] += dd[0]
                dpos[1] += dd[1]

                if boundscheck(seats, dpos):
                    break
                if seats[dpos[0]][dpos[1]] == "L":
                    break
                elif seats[dpos[0]][dpos[1]] == "#":
                    ocp +=1
                    break

    return ocp

def fillchairs(seats, part2):
    stable = False
    while not stable:
        seatcng = {}
        for dy in seats:
            for dx in seats[dy]:
                if seats[dy][dx] == "L":
                    if cntadjseats(seats, [dy,dx], part2) == 0:
                        if dy not in seatcng:
                            seatcng[dy] = {}
                        seatcng[dy][dx] = "#"
                elif seats[dy][dx] == "#":
                    if (cntadjseats(seats, [dy,dx], part2) >= 4 and not part2) or \
                        (cntadjseats(seats, [dy,dx], part2) >= 5 and part2):
                        if dy not in seatcng:
                            seatcng[dy] = {} 
                        seatcng[dy][dx] = "L"
        
        if len(seatcng) == 0:
            stable = True
        else:
            for uy in seatcng:
                seats[uy].update(seatcng[uy])
            #print(seats)
            #input()

    occsum = 0
    for cy in seats:
        occsum += sum(value == "#" for value in seats[cy].values())
    return occsum

part1 = fillchairs(deepcopy(inp), False)
print("Occupied seats at equalibrium:> ", part1)
part2 = fillchairs(deepcopy(inp), True)
print("Occupied seats at equalibrium (with rays):> ", part2)

## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)