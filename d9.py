import time
st = time.time()

inputfile = "input9.txt"
#preamb = 5
preamb = 25

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
xmaslist = []
missing = 0
for i in range(0, preamb):
    xmaslist.append(inp[i])

for o in range(preamb, len(inp)):
    found = False
    for p in xmaslist: 
        s = inp[o] - p
        if s in xmaslist and inp[o] != s:
            found = True
            xmaslist.append(inp[o])
            xmaslist.pop(0)
            break
    if not found:
        missing = inp[o]
        break


print("Invalid number in list:> ", missing)
contiglist = []
xfound = False

for x in range(len(inp)-1, 0, -1):
    if inp[x] < missing:
        contiglist.append(inp[x])
        for y in range(x-1, 0, -1):
            contiglist.append(inp[y])
            if sum(contiglist) == missing:
                found = True
                break
            if sum(contiglist) > missing:
                break
        if found:
            break
        contiglist.clear()

print("Part 2 lol:> ", min(contiglist) + max(contiglist))

## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)