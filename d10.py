import time
from collections import defaultdict
st = time.time()

inputfile = "input10.txt"

def readinput():
    L = []
    with open(inputfile) as fp:
        for line in fp:
            line = line.strip()

            L.append(int(line))
            
    return L

def splitinput():
    L = [i.split("\n") for i in open(inputfile).read().split("\n\n")]

    return L

## Parse input
inp = readinput()
#inp = splitinput()

## Solve problem
inp.sort()
sj = 0
inp.append(max(inp)+3)

# part 1 was piss easy, did that myself no problem
##
# I needed a hint for part two, it didn't make sense to me.
# Basically, you're going down the list of numbers counting the number of paths back to
# the start point (0), and that number is the sum connections from the largest gap to
# the smallest gap. Looking at the list 0, 1, 4, 5, 6, 7, 10 from the example.
# 0 has 1 path to 0 (it is 0 length, but still a path)
# 1 has 1 path to 0 (sum 0)
# 2 does not exist (0)
# 3 does not exist (0)
# 4 has 1 path (sum 1,2,3)
# 5 has 1 path (sum 2,3,4)
# 6 has 2 paths (sum 3,4,5)
# 7 has 4 paths (sum 4,5,6)
# 8 does not exist (0)
# 9 does not exist (0)
# 10 has 4 paths (sum 7,8,9)
# We use a defaultdict because it will return 0 on keys not present in the dict.
# You could also use gaps 1-5 and x-1 to x-5, or gaps 4-7 with x-4 to x-7 but I don't
# think it works properly if there were negative numbers. Anyway, I learned something.
##
#1,3
difs = [0,0]
mdif = [1,3]
prev = sj
dp = defaultdict(int)
dp[sj] = 1
for x in inp:
    if x - prev == mdif[0]:
        difs[0] += 1
    if x - prev == mdif[1]:
        difs[1] += 1
    prev = x

    for d in range(mdif[0], mdif[1]+1):
        dp[x] += dp[x-d]

print("Product of 1-jolt and 3-jolt diffs:> ", difs[0] * difs[1])
print("No. of distict arrangements of adapters:> ", dp[max(inp)])


## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)