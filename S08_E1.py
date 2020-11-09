c,k=input().split()
c=int(c)
k=int(k)
j=1
a=1
while j<=c:
    a*=j
    j+=1
i=1
b=1
while i<=k:
    b*=i
    i+=1
i=1
d=1
while i<=c-k:
    d*=i
    i+=1
print(a/(b*d))
    
