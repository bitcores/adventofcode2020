import time

st = time.time()

inp = []
inp2 = []

## Parse input
group = []
groupset = set()
with open("input6.txt") as fp:
    for line in fp:
        line = line.strip()
        
        if line == "":
            inp.append(group)
            inp2.append(groupset)
            group = []
            groupset = set()
        else:
            group.append(line)
            for x in line:
                groupset.add(x)
    if group[0] != "":
        inp.append(group)
        inp2.append(groupset)

## Solve problem
total = 0
for y in inp2:
    total += len(y)

total2 = 0
for y in inp:
    for c in y[0]:
        ct = 0
        for z in y:
            if c in z:
                ct += 1
        if ct == len(y):
            total2 += 1

print(total)
print(total2)


## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)