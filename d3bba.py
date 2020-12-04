import time
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

st = time.time()

## Functions
def findtrees(slope):
    pos = [0,0]
    ts = 0
    while pos[0] < len(inp):
        if inp[pos[0]][pos[1]] == "#":
            ts += 1
        pos[1] = (pos[1]+slope[1]) % xlen
        pos[0] += slope[0] 
    return ts

if rank == 0:
    inp = []
    down = [1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 47]
    right = [2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 32, 36, 48, 54, 64]
    slopes = []

    ## Parse input
    with open("input3bb.txt") as fp:
        for line in fp:
            line = line.strip()
            
            inp.append(line)

    for y in down:
        for x in right:
            slopes.append([y,x])

    slopet = np.array_split(slopes, size)
else:
    inp = None
    slopet = None

inp = comm.bcast(inp, root=0)
slopet = comm.scatter(slopet, root=0)

## Solve problem
#[y,x]
xlen = len(inp[0])

tl = []
prod = 1
for s in slopet:
    trees = findtrees(s)
    tl.append(trees)
    prod *= trees

sumlist = comm.gather(tl, root=0)
prods = comm.gather(prod, root=0)

if rank == 0:
    bbsum = 1
    for o in prods: 
        bbsum *= o
    print("Product of Bigboy Trees encountered:> ", bbsum)
    print(sumlist)
    #print(sum(sumlist))

    ## Print runtime
    et = time.time()
    if (et - st) < 1:
        rt = str(round((et - st) * 1000,3)) + "ms"
    else:
        rt = str(round(et - st,3)) + "s"
    print("Runtime:> ", rt)
