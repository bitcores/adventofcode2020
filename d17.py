import time
from collections import defaultdict
from copy import deepcopy
st = time.time()

inputfile = "input17.txt"

def readinput():
    L = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: "."))))
    w = 0
    z = 0
    y = 0
    with open(inputfile) as fp:
        for line in fp:
            line = line.strip()

            for x,v in enumerate(line):
                L[w][z][y][x] = v
            y += 1
            
    return L

def splitinput():
    L = [i.split("\n") for i in open(inputfile).read().split("\n\n")]

    return L

## Parse input
inp = readinput()
#inp = splitinput()

## Solve problem
conway = deepcopy(inp)

def printslices():
    for w in conway:
        for z in conway[w]:
            print(z)
            for y in range(ymm[0], ymm[1]+1):
                line = ""
                for x in range(xmm[0], xmm[1]+1):
                    line += conway[w][z][y][x]
                print(line)

def spotval(pos):
    if not pos[0] in conway:
        return "."
    if not pos[1] in conway[pos[0]]:
        return "."
    if not pos[2] in conway[pos[0]][pos[1]]:
        return "."
    if not pos[3] in conway[pos[0]][pos[1]][pos[2]]:
        return "."
    return conway[pos[0]][pos[1]][pos[2]][pos[3]]

def checkneighbors(pos):
    nbr = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1], [0,0]]
    posw, posz, posy, posx = pos[0], pos[1], pos[2], pos[3]
    actvcnt = 0
    for cw in range(-1, 2):
        for cz in range(-1, 2):
            for nn in nbr:
                if cz == 0 and nn == [0,0] and cw == 0:
                    continue
                if not posw+cw in conway:
                    continue
                if not posz+cz in conway[posw+cw]:
                    continue
                if not posy+nn[0] in conway[posw+cw][posz+cz]:
                    continue
                if not posx+nn[1] in conway[posw+cw][posz+cz][posy+nn[0]]:
                    continue
                if conway[posw+cw][posz+cz][posy+nn[0]][posx+nn[1]] == "#":
                    actvcnt += 1
    return actvcnt

## store min/max bounds for z.y.x before start of loop and then update from updatelist


wmm = [min(conway), max(conway)]
zmm = [min(conway[0]), max(conway[0])]
ymm = [min(conway[0][0]), max(conway[0][0])]
xmm = [min(conway[0][0][0]), max(conway[0][0][0])]

for _ in range(0,6):
    
    updatelist = []
    # set ddw range to 0,1 for part 1, wmm[0]-1, wmm[1]+2 for part 2
    for ddw in range(wmm[0]-1, wmm[1]+2):
        for ddz in range(zmm[0]-1, zmm[1]+2):
            for ddy in range(ymm[0]-1, ymm[1]+2):
                for ddx in range(xmm[0]-1, xmm[1]+2):
                    res = checkneighbors([ddw,ddz,ddy,ddx])
                    if spotval([ddw,ddz,ddy,ddx]) == ".":
                        if res == 3:
                            updatelist.append(([ddw,ddz,ddy,ddx], "#"))
                    if spotval([ddw,ddz,ddy,ddx]) == "#":
                        if not res == 2 and not res == 3:
                            updatelist.append(([ddw,ddz,ddy,ddx], "."))  

    for rl in updatelist:
        pos = rl[0]
        pw,pz,py,px = pos[0],pos[1],pos[2],pos[3]
        if not wmm[0] <= pw <= wmm[1]:
            if pw < wmm[0]:
                wmm[0] = pw
            if pw > wmm[1]:
                wmm[1] = pw
        if not zmm[0] <= pz <= zmm[1]:
            if pz < zmm[0]:
                zmm[0] = pz
            if pz > zmm[1]:
                zmm[1] = pz
        if not ymm[0] <= py <= ymm[1]:
            if py < ymm[0]:
                ymm[0] = py
            if py > ymm[1]:
                ymm[1] = py 
        if not xmm[0] <= px <= xmm[1]:
            if px < xmm[0]:
                xmm[0] = px
            if px > xmm[1]:
                xmm[1] = px  
        conway[pw][pz][py][px] = rl[1]

    #printslices()
    #input()

sumcube = 0
for w in conway:
    for z in conway[w]:
        for y in conway[w][z]:
            sumcube += sum(value == "#" for value in conway[w][z][y].values())
#print(updatelist)
print(sumcube)


## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)