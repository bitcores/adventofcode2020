import time
from copy import deepcopy
st = time.time()

inputfile = "input23.txt"

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
p = 0
p1 = deepcopy(inp)
for i in p1:
    for e in range(100):
        holder = i[p+1:p+4]
        i = i[:p+1]+i[p+4:]
        c = int(i[p])
        x = -1
        while x < 0:
            c -= 1
            if c < 0:
                c = 9
            x = i.find(str(c))
        
        i = i[:x+1]+holder+i[x+1:]
        i = i[1:] + i[0]
        
    print("Part1:> ", i[1:])

#fukit, linked list
# this is my node. it holds a value and a pointer to the next node
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

lg = []
p2 = deepcopy(inp)
for i in p2:
    for n in i:
        lg.append(int(n))
    mn = min(lg)
    for nn in range(10, 1000001):
        lg.append(nn)
    mx = lg[-1]
    
    # this is my node dictionary
    # it holds the node for each value
    dnode = {}
    root, last = None,None
    # iterate through all the values
    for n in lg:
        # create a node for the value
        node = Node(n)
        # if this is not the first node created, add this node to the previous node
        # otherwise, this is the root node
        if not last == None:
            last.next = node
        else:
            root = node
        # add the node to the dictionary
        dnode[n] = node
        # set the node as the previous node assigned
        last = node
    # set the root node as the next node of the last node
    # the linked list is now circular
    last.next = root

    pos = root
    for mv in range(10000000):
        # get the node references we need up here first
        hold = pos.next
        holdtail = pos.next.next.next
        nextnode = pos.next.next.next.next
        # build a set of values that are to be "moved"
        holder = set()
        holder.add(hold.val)
        holder.add(hold.next.val)
        holder.add(hold.next.next.val)

        # find the destination value
        destv = pos.val - 1
        while destv in holder or destv < mn:
            destv = destv - 1
            if destv < mn:
                destv = mx

        # get the destination node
        destn = dnode[destv]
        # the "next" node from here will become the first node in holder
        temp = destn.next
        destn.next = hold
        # the "next" node from end of holder will become the previous "next" node in destn
        holdtail.next = temp   

        # the current node now connect to the node which was beyond holder
        pos.next = nextnode
        # the current node now switches to the next node
        pos = nextnode

    print("Part 2:> ", dnode[1].next.val * dnode[1].next.next.val)



## Print runtime
et = time.time()
if (et - st) < 1:
    rt = str(round((et - st) * 1000,3)) + "ms"
else:
    rt = str(round(et - st,3)) + "s"
print("Runtime:> ", rt)