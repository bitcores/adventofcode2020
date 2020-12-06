import time

st = time.time()

inputfile = "input6.txt"

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
    total += len(set.union(*[set(person) for person in group]))
    total2 += len(set.intersection(*[set(person) for person in group]))

print("Sum of questions anyone answered Yes:> ", total)
print("Sum of questions entire groups answered Yes:> ", total2)


## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)