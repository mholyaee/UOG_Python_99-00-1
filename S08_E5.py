def getPower(n,m):
    if n<m:
        n,m=m,n
    i=1
    P=1
    for i in range(m):
        P*=n
    return P
n=int(input('>'))
for i in range(n):
    a,b=input().split()
    a=int(a)
    b=int(b)
    r=getPower(a,b)
    print(r)
