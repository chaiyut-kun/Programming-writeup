import re
upper , lower = 0 , 0
word : str= re.sub("[\s!]","",input())
for e in word:
    if e == " ":
        continue
    else:
        if e.isupper():
            upper+=1
        else:
            lower+=1


print("UPPER:{0}\nLOWER:{1}".format(upper , lower))
        

