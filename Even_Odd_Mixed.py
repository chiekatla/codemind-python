n=input()
s=[]
for i in n:
    s.append(int(i))
e=0
o=0
for i in s:
    if(i%2==0):
        e=e+1
    else:
        o=o+1
if(o>=1 and e>=1):
    print("Mixed")
elif(o==len(s) and e==0):
    print("Odd")
elif(e==len(s) and o==0):
    print("Even")
    