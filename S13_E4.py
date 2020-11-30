# Using Insert method
L=list()
i=0
print("Input 10 numbers which are sorted")
while i<10:
    L.append(int(input()))
    i+=1
x=int(input("Enter X:"))
ind=0
for i in L:
    if i<x:
        break
    ind+=1
L.insert(ind,x)
print(L)