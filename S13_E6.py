def ListConcat(L1,L2):
    L3=list()
    i,j=0,0
    while i <(len(L1)) and j <(len(L2)):
        if L1[i]<L2[j]:
            L3.append(L1[i])
            i+=1
        elif L1[i]>L2[j]:
            L3.append(L2[j])
            j+=1
        else:
            L3.append(L2[j])
            i+=1
            j+=1
    while i < (len(L1)):
        L3.append(L1[i])
        i+=1
    while j<len(L2):
        L3.append(L2[j])
        j+=1
    return L3

L1=list()
L2=list()
n1=int(input("Size of the first list:"))
for i in range(n1):
    L1.append(int(input("The measure:")))
n2=int(input("Size of the second list:"))
for i in range(n2):
    L2.append(int(input("The measure:")))
L1=ListConcat(L1,L2)
print(L1)