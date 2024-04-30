k=int(input())
n=1

while n<k:
	n*=2

count=0
s=0
d=n
if not n==k:
	while not s==k:
		di=d//2
		if s+di<=k:
			s+=di
		d/=2
		count+=1

print(n,count)