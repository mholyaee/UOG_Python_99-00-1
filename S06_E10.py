avg=0
Sum=0
Sumv=0
n=int(input('>'))
for i in range(n):
    grade=float(input('>'))
    v=int(input('>'))
    Sum+=grade*v
    Sumv+=v
print('The average is:', Sum/Sumv)

    
