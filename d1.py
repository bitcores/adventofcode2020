import time
from copy import deepcopy

st = time.time()

inp = []

## Parse input
with open("input1.txt") as fp:
    for line in fp:
        line = line.strip()

        inp.append(int(line))

## Solve problem
finp = sorted(inp)
rinp = sorted(inp, reverse=True)
found = False
for x in finp:
    for y in rinp:
        if finp.count(x) == 1 and x == y:
            continue

        if x + y == 2020:
            found = True
            print("Part 1 result:> ", x * y)
            break
    if found:
        break

found = False
for x in finp:
    for y in rinp:
        for z in finp:
            if finp.count(x) == 1 and (x == y or x == z):
                continue

            if x + y + z == 2020:
                found = True
                print("Part 2 result:> ", x * y * z)
                break
        if found:
            break
    if found:
        break


## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 100,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)