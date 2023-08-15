from sys import stdin
n=int(stdin.readline().rstrip())
narr=list(map(int,stdin.readline().rstrip().split()))
cnt=dict()
for i in narr:
    if not i in cnt:
        cnt[i]=1
    else:
        cnt[i]+=1

# print(cnt.keys())
# k=cnt.keys()
# for i in k:
#     print(cnt[i])

m=int(stdin.readline().rstrip())
marr=list(map(int,stdin.readline().rstrip().split()))
for i in marr:
    if i in cnt:
        print(cnt[i],end=" ")
    else:
        print(0,end=" ")