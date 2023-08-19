from sys import stdin
n=int(stdin.readline().rstrip())
arr=list(map(int,stdin.readline().rstrip().split()))
sarr=sorted(set(arr))
carr=dict()

for i in range(len(sarr)-1,-1,-1):
    j=sarr.pop()
    carr[j]=i

for i in arr:
    print(carr[i],end=" ")