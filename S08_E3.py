def getBSc(avg,nC):
    return avg*0.8+nC*0.2
def getMSc(avg, nP):
    return avg*0.6+nP*0.4
Bscore=0
nb=0
MaxB=0
Mscore=0
nm=0
MaxM=0
while True:
    Type=input('Type of student (b/m):')
    if Type=='b':
        avg,nC=input().split()
        avg=float(avg)
        nC=int(nC)
        Score=getBSc(avg,nC)
        Bscore+=Score
        nb+=1
        if MaxB<Score:
            MaxB=Score
    elif Type=='m':
        avg,nP=input().split()
        avg=float(avg)
        nP=int(nP)
        Score=getMSc(avg,nP)
        Mscore+=Score
        nm+=1
        if MaxM<Score:
            MaxM=Score
    else:
        break

print('\nBachelor Students:')
print('Max Score is:',MaxB)
print('Average of scores is:',Bscore/nb)
print('\nMaster Students:')
print('Max Score is:',MaxM)
print('Average of scores is:',Mscore/nm)
