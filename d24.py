import time
from collections import defaultdict
st = time.time()

inputfile = "input24.txt"

def readinput():
    L = []
    with open(inputfile) as fp:
        for line in fp:
            line = line.strip()

            L.append(line)
            
    return L

def splitinput():
    L = [i.split("\n") for i in open(inputfile).read().split("\n\n")]

    return L

## Parse input
inp = readinput()
#inp = splitinput()

## Solve problem
md = { "e": [0,2], "w": [0,-2], "ne": [1,1], "nw": [1,-1], "se": [-1,1], "sw": [-1,-1] }

tiles = {}
for x in inp:
    m = ""
    pos = [0,0]
    for y in x:
        m += y
        if y == "s" or y == "n":
            continue
        
        if m in md:
            pos[0], pos[1] = pos[0]+md[m][0],pos[1]+md[m][1]
            m = ""
        else:
            print("wtf")
    if not pos[0] in tiles:
        tiles[pos[0]] = {}
    if not pos[1] in tiles[pos[0]]:
        tiles[pos[0]][pos[1]] = "#"
    else:
        if tiles[pos[0]][pos[1]] == "#":
            tiles[pos[0]][pos[1]] = "."
        else:
            tiles[pos[0]][pos[1]] = "#"


bsum = 0
for ys in tiles:
    bsum += sum(value == "#" for value in tiles[ys].values())
print("Part 1:> ", bsum)

def chkwhte(w):
    global changes

    bcc = 0
    white = False
    if not w[0] in tiles:
        white = True
    else:
        if not w[1] in tiles[w[0]]:
            white = True
        elif tiles[w[0]][w[1]] == ".":
            white = True

    if white:
        for mm in md:
            wys,wxs = w[0]+md[mm][0],w[1]+md[mm][1]
            if wys in tiles:
                if wxs in tiles[wys] and tiles[wys][wxs] == "#":
                    bcc += 1
        if bcc == 2:
            changes[w[0]][w[1]] = "#"


for _ in range(100):
    changes = defaultdict(dict)
    for ys in tiles:
        for xs in tiles[ys]:
            bc = 0
            if tiles[ys][xs] == "#":
                for m in md:
                    yys,xxs = ys+md[m][0],xs+md[m][1]
                    if yys in tiles:
                        if xxs in tiles[yys] and tiles[yys][xxs] == "#":
                            bc += 1
                        else:
                            chkwhte([yys,xxs])
                    else:
                        chkwhte([yys,xxs])
                if bc == 0 or bc > 2:
                    changes[ys][xs] = "."
    
    for ny in changes:
        for nx in changes[ny]:
            if not ny in tiles:
                tiles[ny] = {}
            tiles[ny][nx] = changes[ny][nx]
            
dsum = 0
for tits in tiles:
    dsum += sum(value == "#" for value in tiles[tits].values())
print("Part 2:>", dsum)



## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)