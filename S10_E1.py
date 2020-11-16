Str=input("Your String:")
i=0
j=0
while i<len(Str):
    if Str[i]=="C":
        if Str[i:i+8]=="Computer":
            j+=1
    i+=1

print(j)
