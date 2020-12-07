L1=list()
n1=int(input("Size of the first list:"))
for i in range(n1):
    L1.append(int(input("The measure:")))

for i in range(len(L1)):
    j=i+1
    while j<len(L1):
        if L1[i]==L1[j]:
            L1.pop(j)
        else:
            j+=1
print(L1)