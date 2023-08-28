import bisect
from sys import stdin
input=stdin.readline
n=int(input())
arr=[]

for i in range(n):
    inp=tuple(map(int,input().split()))
    arr.append(inp)

arr.sort(key=lambda x:x[1])
l=[0]
lt=[(0,0)]

for i in arr:
    a,b=i
    if l[-1]<a:
        l.append(a)
        lt.append((a,len(l)-1))
    else:
        p=bisect.bisect_left(l,a)
        l[p]=a
        lt.append((a,p))

target=len(l)-1
darr=[]

for i in lt[::-1]:
    if i[1]==target:
        target-=1
    else:
        darr.append(i[0])

# print(darr)
darr.sort()
print(len(darr))
for i in darr:
    print(i)