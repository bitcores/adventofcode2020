import time
st = time.time()

inputfile = "input18.txt"

def readinput():
    L = open(inputfile).read().split("\n")

    return L

def splitinput():
    L = [i.split("\n") for i in open(inputfile).read().split("\n\n")]

    return L

## Parse input
inp = readinput()
#inp = splitinput()

## Solve problem
popen = []
pclose = []

def docalc(op, o1, o2):
    if op == "+":
        return o1 + o2
    if op == "*":
        return o1 * o2

tsum = 0
for x in inp:
    spos = 0
    while True:
        spos = x.find(")", spos)
        if spos > 0:
            opos = x.rfind("(", 0, spos)
            #print(x[opos:spos+1])
            para = x[opos+1:spos]
            splits = para.split(" ")
            while "+" in splits:
                i = splits.index("+")
                splits[i-1] = docalc(splits[i], int(splits[i-1]), int(splits[i+1]))
                splits.pop(i)
                splits.pop(i)
            while len(splits) > 1:
                splits[0] = docalc(splits[1], int(splits[0]), int(splits[2]))
                splits.pop(1)
                splits.pop(1)
            x = x[:opos] + str(splits[0]) + x[spos+1:]
            #print(x)
            spos = opos
        else:
            break

    splits = x.split(" ")
    while "+" in splits:
        i = splits.index("+")
        splits[i-1] = docalc(splits[i], int(splits[i-1]), int(splits[i+1]))
        splits.pop(i)
        splits.pop(i)
    while len(splits) > 1:
        splits[0] = docalc(splits[1], int(splits[0]), int(splits[2]))
        splits.pop(1)
        splits.pop(1)
    #print(splits[0])
    tsum += splits[0]
print(tsum)


## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)