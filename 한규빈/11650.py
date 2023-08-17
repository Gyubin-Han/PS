from sys import stdin
n=int(stdin.readline().rstrip())
arr=[]

for _ in range(n):
    a,b=map(int,stdin.readline().rstrip().split())
    arr.append((a,b))

arr.sort(key=lambda x:(x[0],x[1]))

for i in arr:
    print(i[0],i[1])