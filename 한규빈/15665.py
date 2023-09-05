n,m=map(int,input().split())
inarr=sorted(list(map(int,input().split())))
arr=[]

def bt():
    if len(arr)==m:
        print(*arr)
        return
    
    l=0
    for i in inarr:
        if i==l:
            continue

        arr.append(i)
        bt()
        arr.pop()
        l=i

bt()