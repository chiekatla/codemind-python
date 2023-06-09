n=int(input())
m=int(input())
for i in range(n,m+1):
    z=str(i)
    m=str(i)
    if(m==z[::-1]):
        print(i,end=" ")