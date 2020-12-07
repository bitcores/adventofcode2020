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
    for b in inp:     
        if key in inp[b].keys():
            cancontain.add(b)
            searchbags(b)

totalbags = 0
def countbags(key, no):
    global totalbags
    keytot = 0
    for z in inp[key]:
        for x in inp[key][z]:
            keytot += int(x)
            countbags(z, int(x)*int(no))
    totalbags += keytot * int(no)

## Parse input
goal = "shiny gold"
inp = readinput()
#inp = splitinput()

## Solve problem
#print(inp)
searchbags(goal)
print(len(cancontain))

countbags(goal, 1)
print(totalbags)

## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)