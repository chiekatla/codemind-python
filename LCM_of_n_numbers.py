def lcm(a,b):
    c=0
    for i in range(2,a*b):
        if i%a==0 and i%b==0:
            return i
            c=c+1
    if c==0:
        return(a*b)
        
n=int(input())
a=list(map(int,input().split()))
c=a[0]
for i in range(1,n-1):
    c=lcm(c,a[i])
    d=lcm(c,a[i+1])
print(d)    