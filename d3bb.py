import time
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

st = time.time()

## Functions
def findtrees(dy):
    ypos = 0
    xpos = [0] * len(right)
    trees = [0] * len(right)

    while ypos < len(inp):
        for dx in range(len(xpos)):
            if inp[ypos][xpos[dx]] == "#":
                trees[dx] += 1
        
        for x in range(len(xpos)):
            xpos[x] = (xpos[x]+right[x]) % xlen
        ypos += dy

    return trees

if rank == 0:
    inp = []
    down = [1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31, 35, 37, 41, 47]

    ## Parse input
    with open("input3bb.txt") as fp:
        for line in fp:
            line = line.strip()
            
            inp.append(line)

    downc = np.array_split(down, size)
else:
    inp = None
    downc = None

inp = comm.bcast(inp, root=0)
downc = comm.scatter(downc, root=0)

## Solve problem
#[y,x]
xlen = len(inp[0])
#movelist = [[1,3], [1,1], [1,5], [1,7], [2,1]]
right =[2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 32, 36, 48, 54, 64]

ml = []
for d in downc: ml.append(findtrees(d))

sumlist = comm.gather(ml, root=0)

if rank == 0:
    bbsum = 1
    for o in sumlist: 
        for p in o:
            for q in p:
                bbsum *= q
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