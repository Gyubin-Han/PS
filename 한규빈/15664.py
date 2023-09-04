n,m=map(int,input().split())
inarr=list(map(int,input().split()))
arr=[]
ch=[False]*n

inarr.sort()

def bt(s):
    if len(arr)==m:
        print(*arr)
        return
    
    l=0
    for i in range(s,n):
        if not ch[i] and l!=inarr[i]:
            ch[i]=True
            arr.append(inarr[i])
            bt(i)
            arr.pop()
            ch[i]=False
            l=inarr[i]

bt(0)