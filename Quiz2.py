while True:
    Op=input("Op=")
    if Op=='$':
        break;
    a,b=(input("numbers:").split())
    a=int(a)
    b=int(b)
    if Op=='+':
        print(a+b)
    elif Op=='-':
        print(a-b)
    elif Op=='*':
        print(a*b)
    else:
        try:
            print(a/b)
        except:
            while b==0:
                print('Try again')
                a,b=(input("numbers:").split())
                a=int(a)
                b=int(b)
            print(a/b)
                
            
