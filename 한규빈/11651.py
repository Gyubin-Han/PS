from sys import stdin
n=int(stdin.readline().rstrip())
arr=[]

for _ in range(n):
    x,y=map(int,stdin.readline().rstrip().split())

    arr.append((x,y))

arr.sort(key=lambda x:(x[1],x[0]))

for i in arr:
    print(*i)