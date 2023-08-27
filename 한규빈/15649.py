n,m=map(int,input().split())
arr=[]
ch=[0]*(n+1)

def bt():
    if len(arr)==m:
        print(*arr)
        return
    
    for i in range(1,n+1):
        if ch[i]==1:
            continue
        arr.append(i)
        ch[i]=1
        bt()
        ch[arr.pop()]=0

bt()