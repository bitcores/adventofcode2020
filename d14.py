import time
import re
from itertools import product
st = time.time()

inputfile = "input14.txt"

def readinput():
    L = {}

    with open(inputfile) as fp:
        for line in fp:
            line = line.strip()
            if "mask" in line:
                ma = line.split(" = ")
                L[ma[1]] = []
            else:
                me = line.split(" = ")
                L[ma[1]].append((int(me[0][4:-1]),int(me[1])))
            #L.append(line)
            
    return L

def splitinput():
    L = [i.split("\n") for i in open(inputfile).read().split("\n\n")]

    return L

## Parse input
inp = readinput()
#inp = splitinput()

## Solve problem
mem = {}

def findi(s, ch):
    return [i for i, l in enumerate(s) if l == ch]

for x in inp:
    ones = findi(x, "1")
    zeros = findi(x, "0")
    for y in inp[x]:
        val = str(bin(y[1]))[2:]
        while len(val) < len(x):
            val = "0" + val
        for o in ones:
            val = val[:o] + "1" + val[o+1:]
        for z in zeros:
            val = val[:z] + "0" + val[z+1:]
        
        mem[y[0]] = int(val, 2)

print(sum(mem.values()))

mem = {}
for x in inp:
    ones = findi(x, "1")
    zeros = findi(x, "0")
    exes = findi(x, "X")
    for y in inp[x]:
        val = str(bin(y[1]))[2:]
        while len(val) < len(x):
            val = "0" + val
        
        allcombs = list(product(["0","1"], repeat=len(exes)))    
        for de in allcombs:
            memaddr = str(bin(y[0]))[2:]
            while len(memaddr) < len(x):
                memaddr = "0" + memaddr
            #print(memaddr)
            for o in ones:
                memaddr = memaddr[:o] + "1" + memaddr[o+1:]
            #print(memaddr)
            for i in range(0, len(exes)):
                memaddr = memaddr[:exes[i]] + de[i] + memaddr[exes[i]+1:]
            #print(memaddr)
            mem[int(memaddr,2)] = int(val,2)
            #input()

#print(mem)
print(sum(mem.values()))

## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)