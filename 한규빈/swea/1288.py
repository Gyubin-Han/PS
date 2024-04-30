t=int(input())

for i in range(1,t+1):
	n=int(input())
	
	check=set()
	x=1
	xn=0
	while True:
		xn=x*n
		for a in str(xn):
			check.add(a)

		if len(check)==10:
			break
		x+=1
	print("#"+str(i),(x*n))
