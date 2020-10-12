a=int(input('First:'))
b=int(input('Second:'))
if a>0 and b>0:
    print('Area:',a*b)
else:
    if a<=0 and b<=0:
        print(' Both of them are not true!')
    elif a<=0:
        print(' The first measure is not correct!')
    else:
        print(' The second measure is not correct!')
