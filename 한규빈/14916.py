n=int(input())
count=0

while n>0 and not n%5==0:
	count+=1
	n-=2

if n>-1 and n%5==0:
	print((n//5)+count)
else:
	print(-1)