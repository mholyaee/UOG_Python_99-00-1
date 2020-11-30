def wordnumber(str):
    n=0
    word=''
    count=0
    for j in str:

        if j==' ' or j=='.' or j==',':
            if len(word)>0:
                n+=1
                print(word, count)
                word=''
                count=0
        else:
            word+=j
            count+=1
    return n

str=input("Enter your string:")
temp=wordnumber(str)
print("The word number is:",temp)
