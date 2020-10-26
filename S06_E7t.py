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
            print('Inputs are not valid')

                
            
