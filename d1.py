import time

st = time.time()

inp = []

## Parse input
with open("input1.txt") as fp:
    for line in fp:
        line = line.strip()

        inp.append(int(line))

## Solve problem
found = False
for x in range(0, len(inp)):
    for y in range(x+1, len(inp)):
        if inp[x] + inp[y] == 2020:
            found = True
            print("Part 1 result:> ", inp[x] * inp[y])
            break
    if found:
        break

found = False
for x in range(0, len(inp)):
    for y in range(x+1, len(inp)):
        for z in range(y+1, len(inp)):
            if inp[x] + inp[y] + inp[z] == 2020:
                found = True
                print("Part 2 result:> ", inp[x] * inp[y] * inp[z])
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