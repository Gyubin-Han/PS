n,m=map(int,input().split())
inarr=list(map(int,input().split()))
arr=[]

inarr.sort()

def bt(p):
    if len(arr)==m:
        print(*arr)
        return
    
    for i in range(p,n):
        arr.append(inarr[i])
        bt(i)
        arr.pop()

bt(0)