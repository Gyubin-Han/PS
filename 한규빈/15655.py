n,m=map(int,input().split())
inarr=list(map(int,input().split()))
arr=[]

inarr.sort()

def bt(s):
    if len(arr)==m:
        print(*arr)
        return
    
    for i in range(s,n):
        v=inarr[i]
        if v in arr:
            continue
        arr.append(v)
        bt(i)
        arr.pop()

bt(0)