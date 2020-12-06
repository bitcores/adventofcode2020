import time
from functools import reduce
st = time.time()

inputfile = "input6t.txt"

def readinput():
    L = open(inputfile).read().split("\n")

    return L

def splitinput():
    L = [i.split("\n") for i in open(inputfile).read().split("\n\n")]

    return L

## Parse input
#inp = readinput()
inp = splitinput()

## Solve problem    
total = 0
total2 = 0
for group in inp:
    for p in range(0, len(group)):
        pset = set()
        for x in group[p]:
            pset.add(x)
        group[p] = pset
    total += len(set.union(*group))
    total2 += len(set.intersection(*group))

print("Sum of questions anyone answered Yes:> ", total)
print("Sum of questions entire groups answered Yes:> ", total2)


## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)