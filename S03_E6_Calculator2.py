a=int(input('the first:'))
b=int(input('Second:'))
op=input('Enter the opreator:')

if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='/':
    try:
        print(a/b)
    except:
        print("It is not possible!")        
else:
    print('Your input is not valid!!')
