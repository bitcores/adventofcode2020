import time
from math import ceil

st = time.time()

inp = []


## Parse input
with open("input5.txt") as fp:
    for line in fp:
        line = line.strip()

        inp.append(line)

## Solve problem
allseats = {}
r = 128
for x in inp:
    seat = [0,0]
    row = [127,0]
    isle = [7,0]
    for y in range(0,7):
        if x[y] == "F":
            row[0] -= ceil((row[0] - row[1]) / 2)
        if x[y] == "B":
            row[1] += ceil((row[0] - row[1]) / 2)
    if x[6] == "F":
        seat[0] = row[0]
    else:
        seat[0] = row[1]

    for y in range(7,9):
        if x[y] == "L":
            isle[0] -= ceil((isle[0] - isle[1]) / 2)
        if x[y] == "R":
            isle[1] += ceil((isle[0] - isle[1]) / 2)

    if x[9] == "R":
        seat[1] = isle[0]
    else:
        seat[1] = isle[1]
    allseats[x] = seat
    #print(seat)

toppass = ""
topval = 0
idlist = []
for o in allseats:
    seatval = allseats[o][0] * 8 + allseats[o][1]
    idlist.append(seatval)
    if seatval > topval:
        topval = seatval
        toppass = o

print(toppass, topval)

idlist.sort()
for x in range(idlist[0],idlist[-1]):
    if not x in idlist:
        if x-1 in idlist and x+1 in idlist:
            print(x)

## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)