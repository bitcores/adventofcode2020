import time
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size


st = time.time()

if rank == 0:
    inp = []

    ## Parse input
    with open("input2bb.txt") as fp:
        for line in fp:
            line = line.strip()

            inp.append(line)
    
    chunk = np.array_split(inp, size)
else:
    chunk = None

chunk = comm.scatter(chunk, root=0)

## Solve problem
part1 = 0
part2 = 0
for x in chunk:
    p = x.split(" ")
    g = p[0].split("-")
    c = p[1][0]
    each = p[2]
    
    if each.count(c) >= int(g[0]) and each.count(c) <= int(g[1]):
        part1 += 1
    if (each[int(g[0])-1] == c or each[int(g[1])-1] == c) and not each[int(g[0])-1] == each[int(g[1])-1]:
        part2 += 1

sol1 = comm.gather(part1, root=0)
sol2 = comm.gather(part2, root=0)

if rank == 0:
    print("Part 1 total valid:> ", sum(sol1))
    print("Part 2 total valid:> ", sum(sol2))

    ## Print runtime
    et = time.time()
    if (et - st) < 1:
        rt = str(round((et - st) * 100,3)) + "ms"
    else:
        rt = str(round(et - st,3)) + "s"
    print("Runtime:> ", rt)