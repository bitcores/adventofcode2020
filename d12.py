import time
st = time.time()

inputfile = "input12.txt"

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
def changedir(a, s):
    global d
    r = s // 90
    if a == "L":
        d += r
        if d > 3:
            d -= 4
    if a == "R":
        d -= r
        if d < 0:
            d += 4
    
    for _ in range(0, r):
        if a == "L":
            wp[0], wp[1] = wp[1], wp[0]*-1
        if a == "R":
            wp[0], wp[1] = wp[1]*-1, wp[0]

def movedir(a, s, p):
    global d

    if a == "E":
        p[1] += dl[0][1] * s
    elif a == "N":
        p[0] += dl[1][0] * s
    elif a == "W":
        p[1] += dl[2][1] * s
    elif a == "S":
        p[0] += dl[3][0] * s

dl = [[0,1], [1,0], [0,-1], [-1,0]]
d = 0
cpos1 = [0,0]
cpos2 = [0,0]
wp = [1,10]
for m in inp:
    a = m[0]
    s = int(m[1:])

    if a == "L" or a == "R":
        changedir(a, s)
    elif a == "F":
        cpos1[0] += dl[d][0] * s
        cpos1[1] += dl[d][1] * s
        cpos2[0] += wp[0] * s
        cpos2[1] += wp[1] * s
    else:
        movedir(a, s, cpos1)
        movedir(a, s, wp)
    
print("Manhattan distance:> ", abs(cpos1[0]) + abs(cpos1[1]))
print("Following waypoint:> ", abs(cpos2[0]) + abs(cpos2[1]))


## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)