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
    nums = nl.split(",")
    for c in range(len(nums)-1):
        lpos[nums[c]] = c
    for i in range(len(nums), t):
        if not nums[-1] in lpos.keys():
            nums.append("0") 
        else:
            idx = len(nums) - 1 - lpos[nums[-1]]
            newnum = str(idx)
            nums.append(newnum)
        lpos[nums[-2]] = len(nums)-2
    return(nums[-1])

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