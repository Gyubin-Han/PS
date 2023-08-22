from sys import stdin
from queue import PriorityQueue
n=int(stdin.readline().rstrip())
pq=PriorityQueue()

for i in range(n):
    inp=int(stdin.readline().rstrip())

    if inp==0:
        if pq.qsize()==0:
            print(0)
        else:
            print(pq.get()[1])
    else:
        v=(abs(inp),inp)
        pq.put(v)