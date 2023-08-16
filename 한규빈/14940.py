from sys import stdin
n,m=map(int,stdin.readline().rstrip().split())
inmap=[[0]*m for _ in range(n)]
visit=[[-1]*m for _ in range(n)]
sx=sy=0

for i in range(n):
    s=list(map(int,stdin.readline().rstrip().split()))
    for j in range(m):
        if s[j]==2:
            sx=i
            sy=j
        elif s[j]==0:
            visit[i][j]=0
        inmap[i][j]=s[j]

dx=[1,0,-1,0]
dy=[0,1,0,-1]
next=[]
next.append((sx,sy))
visit[sx][sy]=0

while len(next)>0:
    now=next.pop(0)
    i=now[0]
    j=now[1]

    for a in range(4):
        ddx=i+dx[a]
        ddy=j+dy[a]

        if ddx==-1 or ddx==n or ddy==-1 or ddy==m:
            continue
        if inmap[ddx][ddy]==1 and visit[ddx][ddy]<=0:
            next.append((ddx,ddy))
            visit[ddx][ddy]=visit[i][j]+1

for i in range(n):
    for j in range(m):
        print(visit[i][j],end=" ")
    print()