a,b,c=(input("Type three numbers:").split())
a=int(a)
b=int(b)
c=int(c)
if a+b>c and a+c>b and b+c>a:
    print("Yes, these measures can construct a tringle")
else:
    print("They can't!")
