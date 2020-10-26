counter=0
while True:
    n=int(input('>'))
    if n==0:
        break
    if n%2==0:
        counter+=1

print('Number of even measures:',counter)
