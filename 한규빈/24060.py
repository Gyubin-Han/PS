import sys

n,k=map(int,sys.stdin.readline().rstrip().split())
oarr=list(map(int,sys.stdin.readline().rstrip().split()))
karr=[]

def merge_sort(l,r):
    if l<r:
        q=int((l+r)/2)
        merge_sort(l,q)
        merge_sort(q+1,r)
        merge(l,q,r)

def merge(l,q,r):
    tarr=[]
    i=l
    j=q+1

    while i<=q and j<=r:
        if oarr[i]<oarr[j]:
            tarr.append(oarr[i])
            karr.append(oarr[i])
            i+=1
        else:
            tarr.append(oarr[j])
            karr.append(oarr[j])
            j+=1
    while i<=q:
        tarr.append(oarr[i])
        karr.append(oarr[i])
        i+=1
    while j<=r:
        tarr.append(oarr[j])
        karr.append(oarr[j])
        j+=1
    
    for t in range(len(tarr)):
        oarr[t+l]=tarr[t]

merge_sort(0,n-1)
if len(karr)<k:
    print(-1)
else:
    print(karr[k-1])