def getAvg(L):
    Avg=list()
    i=1
    while i<len(L):
        Avg.append(sum(L[i])/len(L[i]))
        i+=2
    TotalAvg=sum(Avg)/len(Avg)
    print("Average of class:",TotalAvg)
    counter=0
    while counter<len(Avg):
        if Avg[counter]>=TotalAvg:
            print(L[counter*2])
        counter+=1
Mylist=list()
while True:    
    name=input('name:')
    if name=="":
        break
    n=int(input('number of grades:'))
    Mylist.append(name)
    gradeList=list()
    for i in range(n):
        gradeList.append(float(input('>')))
    Mylist.append(gradeList)
getAvg(Mylist)

    
        
        

        

    
        
