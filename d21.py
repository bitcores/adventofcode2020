import time
from copy import deepcopy
st = time.time()

inputfile = "input21.txt"

def readinput():
    L = []
    with open(inputfile) as fp:
        for line in fp:
            line = line.strip()

            L.append(line)
            
    return L

def splitinput():
    L = [i.split("\n") for i in open(inputfile).read().split("\n\n")]

    return L

## Parse input
inp = readinput()
#inp = splitinput()

## Solve problem
food = {}
aller = {}
probset = {}
pairs = {}
algen = set()
for i,x in enumerate(inp):
    foodall = x.split(" (contains ")
    ing = foodall[0].split(" ")
    food[i] = set(ing)
    allergens = foodall[1][:-1].split(", ")
    aller[i] = set(allergens)
    for a in allergens:
        algen.add(a)

#print(food)
#print(aller)
#print(ingred)
#print(algen)
#input()

while len(algen) > 0:
    for f in food:
        for a in aller[f]:
            if not a in probset:
                probset[a] = deepcopy(food[f])
            else:
                probset[a] = probset[a].intersection(food[f])                        
                    
            if len(probset[a]) == 1:
                al = probset[a].pop()
                pairs[a] = al
                for ff in food:
                    if al in food[ff]:
                        food[ff].remove(al)
                algen.remove(a)

nonaling = 0
for e in food:
    nonaling += len(food[e])
print("Part 1:> ", nonaling)

keys = list(pairs.keys())
keys.sort()

death = ""
for e in keys:
    death += pairs[e] + ","

print("Part 2:> ", death[:-1])


## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)