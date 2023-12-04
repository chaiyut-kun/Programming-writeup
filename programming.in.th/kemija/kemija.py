print()
# word = input()
# pattern = r"[a|e|i|o|u]p[a|e|i|o|u]"
# rex_split = re.split(pattern , word)
# rex_find = re.findall(pattern,word)

# decoder = lambda x : x[0]
# map_found = list(map(decoder , rex_find ))
# ans_zip = list(zip(rex_split,map_found))
# ans_join = "".join(list(map("".join , ans_zip)))
# print(ans_join.strip())



words = input("ข้อความที่เข้ารหัส :> ")

vowel = ["apa","epe","ipi","opo","upu"]


def fix(detect : list , word : str ):
    for i in detect:
        word = word.replace( i , i[0] )
    print("ข้อความที่ถอดรหัสแล้ว :> ",word , sep=" ")


fix(vowel , words)



    

  
    

    
    
