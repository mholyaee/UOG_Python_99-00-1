# Runner Program

time=input('Please enter duration:')
IntTime=int(time);
Hour=int(IntTime/3600)# Beacuse 1 hour equals with 3600 seconds!
# Or type: Hour=IntTime//3600
R=IntTime%3600
Minute=R//60
Second=R%60
print(' Javad have run for:',Hour,':',Minute,':',Second)
