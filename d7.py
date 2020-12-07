import time
from copy import deepcopy
st = time.time()

inputfile = "input7.txt"

def readinput():
    assocdict = {}
    with open(inputfile) as fp:
        for line in fp:
            line = line.strip()
            br = line.split(" bags contain ")
            bagdict = {}
            if not br[1] == "no other bags.":
                ib = br[1].split(",")
                for y in ib:
                    ibb = y.strip().split(" ")
                    bagdict[ibb[1]+" "+ibb[2]] = ibb[0]
            assocdict[br[0]] = bagdict
    return assocdict

def splitinput():
    L = [i.split("\n") for i in open(inputfile).read().split("\n\n")]

    return L

cancontain = set()
def searchbags(key):
    gk = []
    gk = deepcopy(key)
    global cancontain

    if goal in inp[key[-1]].keys():
        cancontain.add(key[0])
        return
    else:
        for z in inp[key[-1]].keys():
            gk.append(z)
            searchbags(gk)

## Parse input
goal = "shiny gold"
inp = readinput()
#inp = splitinput()

## Solve problem
#print(inp)

for x in inp:
    searchbags([x])

plist = []
for z in cancontain:
    if z in inp.keys():
        plist.append(z)

#print(plist)
print(len(plist))

totalbags = 0
def countbags(key, no):
    global totalbags
    keytot = 0
    for z in inp[key]:
        for x in inp[key][z]:
            keytot += int(x)
            countbags(z, int(x)*int(no))
    totalbags += keytot * int(no)


countbags(goal, 1)

print(totalbags)

## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)