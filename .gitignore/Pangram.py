str=input ('enter string:')
alph="abcdefghijklmnopqrstuvwxyz
for i in alph:
    if i not in str.lower()|:
        x=0
        break
    else:
        x=1
if(x==1):
    print ("it is pangram")
else:
    print ("it is not pangram")
