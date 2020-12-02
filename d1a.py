import time
from itertools import combinations

st = time.time()

#target = 2020
target = 99920044
inp = []

## Parse input
with open("input1bb3.txt") as fp:
    for line in fp:
        line = line.strip()

        inp.append(int(line))

## Solve problem
f1 = False
f2 = False
inp.sort()
combs = combinations(inp, 2)
for x in combs:
    xy = sum(x)
    if not f1:
        if xy == target:
            f1 = True
            print("Part 1 result:> ", x[0] * x[1] , "("+str(x[0])+"*"+str(x[1])+")")
    if not f2:
        if (target - xy) in inp:
            f2 = True
            print("Part 2 result:> ", x[0] * x[1] * (target - xy) , "("+str(x[0])+"*"+str(x[1])+"*"+str((target - xy))+")")
    
    if f1 and f2:
        break

## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)