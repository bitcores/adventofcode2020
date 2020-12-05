import time

st = time.time()

inp = []


## Parse input
with open("input5.txt") as fp:
    for line in fp:
        line = line.strip()

        inp.append(line)

## Solve problem
def strbin(bstr):
    bout = 0
    for p in bstr:
        bout = bout << 1
        bout += int(p)
    return bout

allseats = []
for x in inp:
    seat = [0,0]
    b = x.translate(str.maketrans("FLBR", "0011"))
    seat[0] = strbin(b[:7])
    seat[1] = strbin(b[7:])

    seatid = seat[0] * 8 + seat[1]
    allseats.append(seatid)

allseats.sort()
topval = allseats[-1]

print("Highest boarding pass seat ID:> ", topval)

myseat = 0

for x in range(allseats[0],allseats[-1]):
    if not x in allseats and (x-1 in allseats and x+1 in allseats):
        myseat = x
        break

print("My seat ID:> ", myseat)

## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)