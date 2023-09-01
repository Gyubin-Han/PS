n,m=map(int,input().split())
inarr=list(map(int,input().split()))
arr=[]

inarr.sort()

def bt():
    if len(arr)==m:
        print(*arr)
        return
    
    for i in inarr:
        arr.append(i)
        bt()
        arr.pop()

bt()