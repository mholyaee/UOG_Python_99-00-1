L=list()
while True:
    n=int(input("Number:"))
    if n<=0:
        break
    L.append(n)
MaxRepeat=0
c=0
for i in range(len(L)):
    j=i+1
    while j<len(L):
        if L[i]==L[j]:
            c+=1
        j+=1
    if MaxRepeat<c:
        MaxRepeat=c
        X=L[i]
    c=0
print("Repeat:",MaxRepeat,"number:",X)