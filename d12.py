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

def movedir(a, s):
    global d

    if a == "F":
        cpos[0] += dl[d][0] * s
        cpos[1] += dl[d][1] * s
    elif a == "E":
        cpos[0] += dl[0][0] * s
        cpos[1] += dl[0][1] * s
    elif a == "N":
        cpos[0] += dl[1][0] * s
        cpos[1] += dl[1][1] * s
    elif a == "W":
        cpos[0] += dl[2][0] * s
        cpos[1] += dl[2][1] * s
    elif a == "S":
        cpos[0] += dl[3][0] * s
        cpos[1] += dl[3][1] * s

def movewp(a, s):
    global d

    if a == "E":
        wp[0] += dl[0][0] * s
        wp[1] += dl[0][1] * s
    elif a == "N":
        wp[0] += dl[1][0] * s
        wp[1] += dl[1][1] * s
    elif a == "W":
        wp[0] += dl[2][0] * s
        wp[1] += dl[2][1] * s
    elif a == "S":
        wp[0] += dl[3][0] * s
        wp[1] += dl[3][1] * s

def rotatewp(a, s):
    global d
    r = s // 90
    nd = d
    if a == "L":
        nd += r
        if nd > 3:
            nd -= 4
    if a == "R":
        nd -= r
        if nd < 0:
            nd += 4

    if r == 2:
        wp[0] = wp[0] * -1
        wp[1] = wp[1] * -1
    elif (a == "L" and r == 1) or (a == "R" and r == 3):
        t = wp[0]
        wp[0] = wp[1]
        wp[1] = t
        if d == 0 or d == 2:
            wp[1] *= -1
        if d == 1 or d == 3:
            wp[1] *= -1
    elif (a == "R" and r == 1) or (a == "L" and r == 3):
        t = wp[1]
        wp[1] = wp[0]
        wp[0] = t
        if d == 0 or d == 2:
            wp[0] *= -1
        if d == 1 or d == 3:
            wp[0] *= -1

    d = nd

dl = [[0,1], [1,0], [0,-1], [-1,0]]
d = 0
cpos = [0,0]
for m in inp:
    a = m[0]
    s = int(m[1:])

    if a == "L" or a == "R":
        changedir(a, s)
    else:
        movedir(a, s)
    
print(abs(cpos[0]) + abs(cpos[1]))

d = 0
wp = [1,10]
cpos = [0,0]
for m in inp:
    a = m[0]
    s = int(m[1:])

    if a == "L" or a == "R":
        rotatewp(a, s)
    elif a == "F":
        cpos[0] += wp[0] * s
        cpos[1] += wp[1] * s
    else:
        movewp(a, s)

print(abs(cpos[0]) + abs(cpos[1]))


## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)