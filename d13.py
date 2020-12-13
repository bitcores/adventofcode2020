import time
from copy import deepcopy

st = time.time()

inputfile = "input13.txt"

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
timestamp = int(inp[0])
buses = inp[1].split(",")

bid = 0
smallest = 999999
for x in buses:
    if x.isdigit():
        dif = timestamp % int(x)
        sep = int(x) - dif
        if sep < smallest:
            smallest = int(sep)
            bid = int(x)
        if dif == 0:
            print("anomoly")

print(smallest * bid)

##
# This is another case where I didn't know how to approach this problem in
# the correct manner and needed help.
# Basically we want to find a number that, + an offset, is a multiple of the
# target number, and without the offset is a multiple of the first number.
# So in the set 3,11,7 the first multiple of 3 that +1 is a multiple of 11 is 21 
# Knowing this, you can take any multiple of 3 and 11 and add 21 to get a multiple
# of 3 that +1 is a multiple of 11.
# So now you can search for a multiple of (3, 11) that +21 +2 is a multiple of 7,
# which is 54
# If we were to add 13 to the list, now we would be looking for a number that is a
# multiple of (3, 11, 7) that +54 +3 is a multiple of 13
# Inherently, this number +54 +2 will be a multiple of 7 and +54 +1 a multiple of 11 
# 
##

constraints = inp[1].split(",")
fac = 0
mul = 1
for i in range(0, len(constraints)):
    if constraints[i] == "x":
        continue
    
    while (fac + i) % int(constraints[i]):
        fac += mul
    mul *= int(constraints[i])
    print(fac, mul)

print(fac)




## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)