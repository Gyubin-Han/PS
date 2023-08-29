n,m=map(int,input().split())
arr=[]

def bt(s):
    if len(arr)==m:
        print(*arr)
        return
    
    for i in range(s,n+1):
        arr.append(i)
        bt(i)
        arr.pop()

bt(1)