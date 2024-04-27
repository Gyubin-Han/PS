n=int(input())

for i in range(n):
	a,b=map(int,input().split())
	result=a+b

	if result>23:
		result-=24
	print("#"+str(i+1),result)
