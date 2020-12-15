import time
st = time.time()

inputfile = "input15.txt"

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
def spitnumber(nl, t):
    lpos = {}
    lnum = []
    nums = nl.split(",")
    for c in range(len(nums)-1):
        lpos[nums[c]] = c
    lnum.insert(0, "X")
    lnum.insert(1, nums[-1])

    for i in range(len(nums), t):
        if not lnum[1] in lpos.keys():
            newnum = "0"
        else:
            idx = i - 1 - lpos[lnum[1]]
            newnum = str(idx)
        lnum[0], lnum[1] = lnum[1], newnum
        lpos[lnum[0]] = i -1

    return(lnum[1])

for x in inp:
    print("Input:> ", x)
    print("Part 1:> ", spitnumber(x, 2020))
    print("Part 2:> ", spitnumber(x, 30000000))

## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)