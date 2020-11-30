# inserting to a descending sorted list
# Using append
def add2list(Mylist,x):
    Mylist.append(x)
    ind=len(Mylist)-1
    while ind>0:
        if Mylist[ind]>Mylist[ind-1]:
            Mylist[ind],Mylist[ind-1]=Mylist[ind-1],Mylist[ind]
        ind-=1
    #return Mylist
print("Input 10 numbers which are sorted\n")
i = 0
L=list()
while i<10:
   L.append(int(input()))
   i+=1
x=int(input("Enter X:"))
add2list(L,x)
print(L)
#print(N)