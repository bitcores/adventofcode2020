import time
st = time.time()
from collections import defaultdict

inputfile = "input16.txt"

def readinput():
    L = open(inputfile).read().split("\n")

    return L

def splitinput():
    L = [i.split("\n") for i in open(inputfile).read().split("\n\n")]

    return L

## Parse input
#inp = readinput()
inp = splitinput()

## Solve problem
def testval(inv):
    for trule in rules:
        for rr in rules[trule]:
            ruv = rr.split("-")
            if int(ruv[0]) <= inv <= int(ruv[1]):
                return False, trule
    return inv, None

def matchrules(valli):
    for y in range(len(valli)):
        matches = []
        for trule in rules:
            dual = []
            for rr in rules[trule]:
                ruv = rr.split("-")
                if not (int(ruv[0]) <= int(valli[y]) <= int(ruv[1])):
                    dual.append(False)
            if dual.count(False) == 2:
                matches.append((trule, y))
        if len(matches) > 0:
            return matches[0]
    return None

rules = {}
tick = []
nearby = []

for x in inp[0]:
    r = x.split(": ")
    rd = r[1].split(" or ")
    rules[r[0]] = rd

tick = inp[1][1]

for x in range(1, len(inp[2])):
    nearby.append(inp[2][x])

invalrate = []
invalid = []
for t in nearby:
    vals = t.split(",")
    for v in vals:
        res,field = testval(int(v))
        invalrate.append(res)
        if not res == False:
            invalid.append(t)

print(sum(invalrate))
#print(len(nearby))

for invl in invalid:
    nearby.remove(invl)

ticvals = defaultdict(lambda: [])
ticfields = {}
for ti in nearby:
    vals = ti.split(",")
    back = matchrules(vals)
    if back != None:
        ticvals[back[0]].append(back[1])

while len(ticfields) < len(rules)-1:
    for x in ticvals:
        matches = []
        for y in range(len(rules)):
            if not y in ticvals[x]:
                matches.append(y)
        if len(matches) == 1:
            ticfields[x] = matches[0]
            for z in ticvals:
                ticvals[z].append(matches[0])


mytick = tick.split(",")
mytickval = 1
for x in ticfields:
    if "departure" in x:
        mytickval *= int(mytick[ticfields[x]])

print(mytickval)

##print(rules)
#p#rint(tick)
#print(nearby)
        


## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)