Fibo=list()
n=int(input('>'))
Fibo.append(1)
Fibo.append(1)
for i in range(2,n):
    X=Fibo[i-1]+Fibo[i-2]
    Fibo.append(X)
for i in range(n):
    print(Fibo[i],'\n')
    
