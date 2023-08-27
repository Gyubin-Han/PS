from sys import stdin
import heapq
n=int(stdin.readline().rstrip())

for a in range(n):
    m=int(stdin.readline().rstrip())
    maxh,minh=[],[]
    isdel=dict()
    cnt=0
    
    for i in range(m):
        s=list(map(str,stdin.readline().rstrip().split()))
        v=int(s[1])

        if s[0]=='I':
                heapq.heappush(maxh,(-v,i))
                heapq.heappush(minh,(v,i))
                isdel[i]=True
                cnt+=1
        else:
            if cnt>0:
                if v==-1:
                    while minh and not isdel[minh[0][1]]:
                        heapq.heappop(minh)
                    d=heapq.heappop(minh)
                else:
                    while maxh and not isdel[maxh[0][1]]:
                        heapq.heappop(maxh)
                    d=heapq.heappop(maxh)
                # print(d[0],d[1])
                isdel[d[1]]=False
                cnt-=1
            else:
                continue
    
    # print(maxh)
    # print(minh)
    while minh and not isdel[minh[0][1]]:
        heapq.heappop(minh)
    while maxh and not isdel[maxh[0][1]]:
        heapq.heappop(maxh)

    # print(maxh)
    # print(minh)
    if cnt>0:
        print(-maxh[0][0],minh[0][0])
    else:
        print("EMPTY")