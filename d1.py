import time
from copy import deepcopy
from itertools import combinations

st = time.time()

inp = []

## Parse input
with open("input1.txt") as fp:
    for line in fp:
        line = line.strip()

        inp.append(int(line))

## Solve problem
comblist = list(combinations(inp,2))
for x in comblist:
    if x[0] + x[1] == 2020:
        print("Part 1 result:> ", x[0] * x[1])
        break

comblist = list(combinations(inp,3))
for x in comblist:
    if x[0] + x[1] + x[2] == 2020:
        print("Part 1 result:> ", x[0] * x[1] * x[2])
        break


## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 100,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)