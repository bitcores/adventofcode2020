import time
from collections import defaultdict
from math import prod
from copy import deepcopy
st = time.time()

inputfile = "input20.txt"

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
#inp = readinput()
inp = splitinput()

## Solve problem
tiles = {}
orient = {}
final = defaultdict(dict)
grid = {}
cons = {}
# each tile is a dict of [y][x]
for t in inp:
    tn = int(t[0][4:-1].strip())
    tiles[tn] = defaultdict(dict)
    orient[tn] = {"r": 0, "v": 0, "h": 0}
    cons[tn] = {}
    grid[tn] = {}
    for ys in range(1, len(t)):
        for i,xs in enumerate(t[ys]):
            tiles[tn][ys-1][i] = xs

def printtile(tile):
    for ys in tile:
        s = ""
        for xs in tile[ys]:
            s += tile[ys][xs]
        print(s)

def printimg(img):
    ky = img.keys()
    for ys in range(min(ky), max(ky)+1):
        print(ys)
        s = defaultdict(str)
        ks = img[ys].keys()
        for xs in range(min(ks), max(ks)+1):
            for yss in tiles[img[ys][xs]]:
                for xss in tiles[img[ys][xs]][yss]:
                        s[yss] += tiles[img[ys][xs]][yss][xss]
                s[yss] += " "
        for l in s:
            print(s[l])
        print(" ")

def getcol(k, c):
    s = ""
    for ys in tiles[k]:
        s += tiles[k][ys][c]
    return s

def getrow(k, r):
    s = ""
    for xs in tiles[k][r]:
        s+= tiles[k][r][xs]
    return s

def checksides(k, l):
    for ts in tiles:
        if ts == k:
            continue
        for crs in cr:
            com = getcol(ts, crs)
            if com == l:
                return ts
            if com[::-1] == l:
                return ts
            com = getrow(ts, crs)
            if com == l:
                return ts
            if com[::-1] == l:
                return ts
    return 0

def rotatetile(k):
    ntile = deepcopy(tiles[k])
    l = len(tiles[k][0]) - 1
    d = 0
    for y in tiles[k]:
        c = l
        for x in tiles[k][y]:
            ntile[c][d] = tiles[k][y][x]
            c -= 1
        d += 1
    return ntile

def hfliptile(k):
    ntile = deepcopy(tiles[k])
    l = len(tiles[k])
    for y in tiles[k]:
        for r in range(0,l):
            ntile[y][r] = tiles[k][y][l-1-r]
    return ntile

def vfliptile(k):
    ntile = deepcopy(tiles[k])
    l = len(tiles[k])
    for r in range(0,l):
        ntile[r] = tiles[k][l-1-r]
    return ntile

def rotateimg():
    global final
    nimg = deepcopy(final)
    l = len(final[0]) - 1
    d = 0
    for y in final:
        c = l
        for x in final[y]:
            nimg[c][d] = final[y][x]
            c -= 1
        d += 1
    final = deepcopy(nimg)

def hflipimg():
    global final
    nimg = deepcopy(final)
    l = len(final)
    for y in final:
        for r in range(0,l):
            nimg[y][r] = final[y][l-1-r]
    final = deepcopy(nimg)

def vflipimg():
    global final
    nimg = deepcopy(final)
    l = len(final)
    for r in range(0,l):
        nimg[r] = final[l-1-r]
    final = deepcopy(nimg)

def fillerow(prvtile, nxttile, uo, fr):
    while nxttile in sid or nxttile in crn:
        grid[nxttile] = [grid[prvtile][0]+uo[0], grid[prvtile][1]+uo[1]]
        if fr:
            frow.append(nxttile)
        if nxttile in crn:
            break
        tmp = nxttile
        for e in cons[nxttile]:
            if cons[nxttile][e] in sid or cons[nxttile][e] in crn:
                if cons[nxttile][e] == prvtile:
                    continue
                nxttile = cons[nxttile][e]
                break
        prvtile = tmp

def fillmrow(prvtile, nxttile, uo):
    cr = deepcopy(grdr[0])

    while nxttile in sid or nxttile in inr:
        grid[nxttile] = [grid[prvtile][0]+uo[0], grid[prvtile][1]+uo[1]]
        if nxttile in sid:
            break
        tmp = nxttile
        for e in cons[nxttile]:
            if cons[nxttile][e] == prvtile:
                ne = e + 2
                if ne > 3:
                    ne -= 4
                break
        nxttile = cons[nxttile][ne]
        prvtile = tmp

def matcher(pt, tt, m, d):
    if m == "c":
        ptc = getcol(pt, cr[1])
    if m == "r":
        if d < 0:
            ptc = getrow(pt, cr[0])
        else:
            ptc = getrow(pt, cr[1])

    
    for s in pro:       
        if "h" in s:
            tiles[tt] = hfliptile(tt)
        if "v" in s:
            tiles[tt] = vfliptile(tt)
        if "r" in s:
            tiles[tt] = rotatetile(tt)

        if m == "c":
            ttc = getcol(tt, cr[0])
        if m == "r":
            if d < 0:
                ttc = getrow(tt, cr[1])
            else:
                ttc = getrow(tt, cr[0])
        #print(ptc, ttc)
        if ptc == ttc:
            return
    input("No match, break out")

def matchimg(s): 
    #print(s)       
    if "h" in s:
        hflipimg()
    if "v" in s:
        vflipimg()
    if "r" in s:
        rotateimg()


corners = []
cr = [0,9]

# left = 0, top = 1, right = 2, bottom = 3
for tk in tiles:
    col = getcol(tk, cr[0])
    s = checksides(tk, col)
    if s > 0:
        cons[tk][0] = s
    col = getcol(tk, cr[1])
    s = checksides(tk, col)
    if s > 0:
        cons[tk][2] = s
    row = getrow(tk, cr[0])
    s = checksides(tk, row)
    if s > 0:
        cons[tk][1] = s
    row = getrow(tk, cr[1])
    s = checksides(tk, row)
    if s > 0:
        cons[tk][3] = s

crn = [k for k,v in cons.items() if len(v) == 2]
sid = [k for k,v in cons.items() if len(v) == 3]
inr = [k for k,v in cons.items() if len(v) == 4]
print("Part 1:> ", prod(crn))


offset = [[0,-1], [-1,0], [0,1], [1,0]]
# build the first row/column
grdr = [0,0]
grid[crn[0]] = [0,0]
frow = []
t = cons[crn[0]]
er = iter(t)
p = next(er)
grdr[0] = p
uo = offset[p]
pt = crn[0]
nt = cons[crn[0]][p]
fillerow(pt, nt, uo, True)

p = next(er)
grdr[1] = p
uo = offset[p]
pt = crn[0]
nt = cons[crn[0]][p]
fillerow(pt, nt, uo, False)


for f in frow:
    if f in sid:
        t = cons[f]
        er = iter(t)
        for p in er:
            if not cons[f][p] in inr:
                continue
            uo = offset[grdr[1]]
            pt = f
            nt = cons[f][p]
            fillmrow(pt, nt, uo)    

    if f in crn:
        t = cons[f]
        er = iter(t)
        for p in er:
            if cons[f][p] in frow:
                continue
            uo = offset[grdr[1]]
            pt = f
            nt = cons[f][p]
            fillerow(pt, nt, uo, False)    

layout = defaultdict(dict)
for ts in grid:
    layout[grid[ts][0]][grid[ts][1]] = ts

#print(layout)


#print(grid)
#print(frow)

# go through each row and check the alignment of the tile next to it
# # processing the block looking for matches
# z: pass, r: rotate, h: flip h, v: flip v
pro = ["z", "r", "h", "hv", "vr", "h", "hv", "vr", "r"]
y = layout.keys()
s,t,r = min(y), max(y)+1, 1
if min(y) < 0:
    s,t,r = max(y), min(y)-1, -1

for ys in range(s, t, r):
    x = layout[ys].keys()
    for xs in range(min(x), max(x)+1):
        if ys == 0 and xs == 0:
            continue

        if xs == 0:
            pt = layout[ys-r][xs]
            tt = layout[ys][xs]
            #print("matching",pt, tt)
            matcher(pt, tt, "r", r)
        else:
            pt = layout[ys][xs-1]
            tt = layout[ys][xs]
            #print("matching", pt, tt )
            matcher(pt, tt, "c", r)

#printimg(layout)

ky = layout.keys()
y = 0
for ys in range(min(ky), max(ky)+1):
    ks = layout[ys].keys()
    s = defaultdict(str)
    for xs in range(min(ks), max(ks)+1):
        for yss in tiles[layout[ys][xs]]:
            if yss == 0 or yss == 9:
                continue
            for xss in tiles[layout[ys][xs]][yss]:
                if xss == 0 or xss == 9:
                    continue
                s[yss] += tiles[layout[ys][xs]][yss][xss]
    for l in s:
        for i,x in enumerate(s[l]):
            final[y][i] = x
        y += 1

#print(final)
#printtile(final)
#print(" ")
#printtile(rotateimg(final))

monster = {0:{18: "#"}, 1:{0: "#", 5: "#", 6: "#", 11: "#", 12: "#", 17: "#", 18: "#", 19: "#"}, \
 2: {1: "#", 4: "#", 7: "#", 10: "#", 13: "#", 16: "#"}}
monsize = 15
for s in pro:
    matchimg(s)
    #printtile(final)
    #input()

    countmon = 0
    for y in range(0, len(final)-2):
        for x in range(0, len(final[y])-19):
            monmatch = 0
            for my in monster:
                for mx in monster[my]:
                    if final[y+my][x+mx] == monster[my][mx]:
                        monmatch += 1
            if monmatch == monsize:
                countmon +=1
                for my in monster:
                    for mx in monster[my]:
                        final[y+my][x+mx] = "O"
    
    if countmon > 0:
        break
    

printtile(final)
print(countmon)
roughwater = 0
for ys in final:
    roughwater += sum(value == "#" for value in final[ys].values())
print(roughwater)




## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)