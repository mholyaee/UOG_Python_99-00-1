n=int(input("The input is:"))
i=2
flag=0
while i<=n/2:
    if n%i==0:
        print("Not Prime!")
        flag=1
        break
    i+=1
if flag==0:
    print("Prime")
