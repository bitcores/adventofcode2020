import time

st = time.time()

inp = []

## Parse input
with open("input3.txt") as fp:
    for line in fp:
        line = line.strip()
        
        inp.append(line)


## Solve problem
#[y,x]
def findtrees(move):
    pos = [0,0]
    ts = 0
    while pos[0] < len(inp):
        if inp[pos[0]][pos[1]] == "#":
            ts += 1
        pos[1] = (pos[1]+move[1]) % len(inp[pos[0]])
        pos[0] += move[0] 
    return ts

p1 = 0
p2 = 1
movelist = [[1,3], [1,1], [1,5], [1,7], [2,1]]

p1 = findtrees(movelist[0])
for m in movelist: p2 *= findtrees(m)

print("Trees encountered part 1:> ", p1)
print("Trees encountered part 2:> ", p2)

## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)