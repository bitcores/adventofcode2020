import time

st = time.time()

inp = []


## Parse input
with open("input2.txt") as fp:
    for line in fp:
        line = line.strip()

        inp.append(line)

## Solve problem
part1 = 0
part2 = 0
for x in inp:
    p = x.split(" ")
    g = p[0].split("-")
    c = p[1][0]
    each = p[2]
    
    if each.count(c) >= int(g[0]) and each.count(c) <= int(g[1]):
        part1 += 1
    if (each[int(g[0])-1] == c or each[int(g[1])-1] == c) and not each[int(g[0])-1] == each[int(g[1])-1]:
        part2 += 1

print("Part 1 total valid:> ", part1)
print("Part 2 total valid:> ", part2)

## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)