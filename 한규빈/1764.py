from sys import stdin
n,m=map(int,stdin.readline().rstrip().split())

noarr=set()
for _ in range(n):
    s=stdin.readline().rstrip()
    noarr.add(s)

carr=[]
for _ in range(m):
    s=stdin.readline().rstrip()

    if s in noarr:
        carr.append(s)

carr.sort()

print(len(carr))
for i in carr:
    print(i)