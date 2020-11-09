def getAvg(n):
    i=1
    Sum=0
    while i<=n:
        g=float(input('>'))
        Sum+=g
        i+=1
    return Sum/n
Maxavg=0
while True:
    n=int(input('Number of courses:'))
    if n<=0:
        break
    avg=getAvg(n)
    if avg>Maxavg:
        Maxavg=avg
print('Average of the TOP student:',Maxavg)
    
