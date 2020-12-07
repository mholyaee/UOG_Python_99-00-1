def ListConcat(L1,L2):
    L1 = L1 + L2
    return L1

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