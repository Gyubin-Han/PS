n=int(input())
arr=[]

for _ in range(n):
    arr.append(tuple(map(int,input().split())))

arr.sort(key=lambda x:(x[1],x[0]))
last=0
count=0

for i in arr:
    if i[0] >= last:
        count+=1
        last=i[1]

print(count)