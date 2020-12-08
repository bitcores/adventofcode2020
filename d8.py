import time
from copy import deepcopy
st = time.time()

inputfile = "input8.txt"

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

def isInt(self, s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def comp(accum, instl, pos, chn, p2):
    while not pos in instl and pos < len(inp):
        instl.append(pos)
        opt = inp[pos].split(" ")
        val = int(opt[1])
        if opt[0] == "nop":
            if chn == 0 and p2:
                t = pos + val             
                ret = comp(accum, deepcopy(instl), t, 1, p2)
                if ret != None:
                    return ret
            pos += 1

        if opt[0] == "acc":
            accum += val
            pos += 1

        if opt[0] == "jmp":
            if chn == 0 and p2:
                t = pos + 1               
                ret = comp(accum, deepcopy(instl), t, 1, p2)
                if ret != None:
                    return ret
            pos += val

    if pos >= len(inp) or not p2:
        return accum

## Parse input
inp = readinput()
#inp = splitinput()

## Solve problem
part1 = comp(0, [], 0, 0, False)
print("Value at loop exception:> ", part1)
part2 = comp(0, [], 0, 0, True)
print("Value at safe exit:> ", part2)

## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)