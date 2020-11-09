def fact(c):
    a=1
    j=1
    while j<=c:
        a*=j
        j+=1
    return a
c,k=input().split()
c=int(c)
k=int(k)
a=fact(c)
b=fact(k)
d=fact(c-k)
print(a/(b*d))
