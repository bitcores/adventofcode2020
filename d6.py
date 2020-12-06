import time
st = time.time()

inputfile = "input6.txt"

def readinput():
    return open(inputfile).read().split("\n")

def splitinput():
    L = open(inputfile).read().split("\n\n")
    for x in range(0, len(L)):
        L[x] = L[x].split("\n")
    return L

## Parse input
#inp = readinput()
inp = splitinput()

## Solve problem
total = 0
for group in inp:
    gset = set()
    for person in group:
        for x in person:
            gset.add(x)
    total += len(gset)

total2 = 0
for group in inp:
    for q in group[0]:
        qt = 0
        for person in group:
            if q in person:
                qt += 1
        if qt == len(group):
            total2 += 1

print("Sum of questions anyone answered Yes:> ", total)
print("Sum of questions entire groups answered Yes:> ", total2)


## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)