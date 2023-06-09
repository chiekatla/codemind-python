n=int(input())
k=[]
for i in range(1,n+1):
    if(n%i==0):
        k.append(i)
z=[]
for i in k:
    i>1
    for j in range(2,i):
        if(i%j==0):
            z.append(i)
            break
print(len(z)+1)        