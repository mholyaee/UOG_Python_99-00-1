Str=input("Input your Email:")
i=0
dot=False
Sign=False
while i<len(Str):
    if Str[i]=='.':
        dot=True
    if Str[i]=='@':
        Sign=True
    i+=1
if dot and Sign:
    print("Your email is valid!")
else:
    print("Not valid!")
