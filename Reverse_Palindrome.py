n=int(input())
for i in range(n):
    n=n+int(str(n)[::-1])
    if n==int(str(n)[::-1]):
        print(n)
        break