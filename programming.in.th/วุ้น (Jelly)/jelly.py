""" 

    สูตร สี่เหลี่ยมมุมฉาก ก * ย * ส
    

"""

value = [int(i) for i in input().split()]
result = 0
for v in value:
    c = 0
    while (v != 1):
        c+=1
        v//=2
    result += c
    
print(result)



