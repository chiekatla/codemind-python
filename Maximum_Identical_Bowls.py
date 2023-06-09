n=int(input())
l=list(map(int,input().split()))
m=sum(l)


while(m%n!=0):
    n=n-1
print(n)    