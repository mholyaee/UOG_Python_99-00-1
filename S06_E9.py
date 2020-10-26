avg=0
maxc=0
for i in [1,2,3,4,5,6,7,8,9,10,11,12]:
    cost=int(input())
    avg+=cost
    if maxc<=cost:
        maxc=cost
        ind=i
print('The max cost has been occured in:',ind)
print('Average is:',avg/12)
             
