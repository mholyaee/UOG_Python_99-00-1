L=list()
Year=list()
while True:
    ST_NO=input('>')
    try:
        n=int(ST_NO[:2])
        try:
            ind=Year.index(n)
            L[ind]=L[ind]+1
        except:
            Year.append(n)
            L.append(1)
                
    except:
          break;
for i in range(len(L)):
    print("year:",Year[i],"=",L[i])
