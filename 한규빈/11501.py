import sys
input=sys.stdin.readline
t=int(input().rstrip())

for _ in range(t):
	d=int(input().rstrip())
	arr=list(map(int,input().rstrip().split()))

	mx=0
	s=0
	for i in range(d):
		a=arr.pop()
		
		if mx<a:
			mx=a
		else:
			s+=(mx-a)
	print(s)