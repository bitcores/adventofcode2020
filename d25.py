import time
st = time.time()

inputfile = "input25.txt"

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
div = 20201227
kd = {}
kd[1] = int(inp[0])
kd[2] = int(inp[1])
kl = {}
sb = 7
n1 = 1
n2 = 1
loop = 1
#print(kd)
while True:
    if len(kl) < 2:
        n1 = n1 * sb % div
        n2 = n2 * sb % div
    else:
        break
    
    if n1 == kd[1]:
        kl[kd[1]] = loop
    if n1 == kd[2]:
        kl[kd[2]] = loop
    if n2 == kd[1]:
        kl[kd[1]] = loop
    if n2 == kd[2]:
        kl[kd[2]] = loop
    loop += 1
    #print(n1, n2)

#print(kd, kl)
d = kd[1]
#print(d)
n = 1
for _ in range(kl[kd[2]]):
    n = n * d % div

print(n)



## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)