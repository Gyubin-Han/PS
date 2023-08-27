from sys import stdin
from collections import deque
n,m=map(int,stdin.readline().rstrip().split())
arr=[['']*m for _ in range(n)]
sx=sy=0

for i in range(n):
    li=stdin.readline().rstrip()
    for j in range(m):
        arr[i][j]=li[j]
        if li[j]=='I':
            sx=i
            sy=j

dx=[1,0,-1,0]
dy=[0,1,0,-1]

cnt=0
next=deque()
next.append((sx,sy))
arr[sx][sy]='C'

while next:
    now=next.pop()

    for i in range(4):
        ddx=now[0]+dx[i]
        ddy=now[1]+dy[i]

        if ddx<0 or ddy<0 or ddx>=n or ddy>=m:
            continue
        c=arr[ddx][ddy]
        if c=='O' or c=='P':
            if c=='P':
                cnt+=1
            next.append((ddx,ddy))
            arr[ddx][ddy]='C'

if cnt==0:
    print('TT')
else:
    print(cnt)