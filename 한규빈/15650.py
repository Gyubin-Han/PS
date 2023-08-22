n,m=map(int,input().split())
arr=[]
ch=[0]*(n+1)

def bt(s):
    if len(arr)==m:
        print(*arr)
        return
    
    for i in range(s,n+1):
        if ch[i]==1:
            continue
        arr.append(i)
        ch[i]=1
        bt(i)
        ch[arr.pop()]=0

bt(1)