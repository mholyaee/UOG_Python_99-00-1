a=int(input('First:'))
b=int(input('Second:'))
if a>0 and b>0:
    print('Area:',a*b)
else:
    if a<=0:
        print(' The first measure is not correct!')
    if b<=0:
        print(' The second measure is not correct!')
