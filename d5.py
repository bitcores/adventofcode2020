import time

st = time.time()

inp = []


## Parse input
with open("input5.txt") as fp:
    for line in fp:
        line = line.strip()

        inp.append(line)

## Solve problem
allseats = []
for x in inp:
    b = x.translate(str.maketrans("FLBR", "0011"))
    allseats.append(int(b, 2))

allseats.sort()
topval = allseats[-1]
print("Highest boarding pass seat ID:> ", topval)

myseat = sorted(set(range(allseats[0], allseats[-1]+1)).difference(allseats))[0]
print("My seat ID:> ", myseat)

## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)