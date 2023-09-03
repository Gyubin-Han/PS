n,m=map(int,input().split())
inarr=list(map(int,input().split()))
arr=[]
ch=[False]*n

inarr.sort()

def bt():
    if len(arr)==m:
        print(*arr)
        return
    
    l=0
    for i in range(n):
        if not ch[i] and l!=inarr[i]:
            ch[i]=True
            l=inarr[i]
            arr.append(l)
            bt()
            ch[i]=False
            arr.pop()

bt()