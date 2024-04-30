n=int(input())

for i in range(1,n+1):
    k=int(input())

    result=0
    for j in range(1,k+1):
        if j%2==0:
            result-=j
        else:
            result+=j
    print("#"+str(i),result)
