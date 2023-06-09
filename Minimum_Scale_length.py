def fun(m,l):
    for i in range(m,0,-1):
        c=0
        for j in l:
            if j%i==0:
                c+=1
        if c==len(l):
            return i
        
n=int(input())
l=list(map(int,input().split()))
m=min(l)
print(fun(m,l))