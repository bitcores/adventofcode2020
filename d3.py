import time

st = time.time()

inp = dict()

y = 0
## Parse input
with open("input3.txt") as fp:
    for line in fp:
        line = line.strip()
        li = []
        for x in line:
            li.append(x)
        inp[y] = li
        y += 1

## Solve problem
#[y,x]
p1 = 0
p2 = 1
movelist = [[3,1], [1,1], [5,1], [7,1], [1,2]]
fr = True
for m in movelist:
    pos = [0,0]
    ts = 0
    while pos[0] < y:
        if len(inp[pos[0]]) <= pos[1]:
            pos[1] -= len(inp[pos[0]])

        if inp[pos[0]][pos[1]] == "#":
            ts += 1
        
        pos[1] += m[0]
        pos[0] += m[1]
    
    p2 = p2 * ts
    if fr:
        p1 = ts
        fr = False

print("Trees encountered part 1:> ", p1)
print("Trees encountered part 2:> ", p2)

## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)