""" 

    กำแพงจะแบ่งเป็นส่วนๆ แต่ละส่วนจะมีด้านที่ขนานกับพื้น (ด้านกว้าง) ยาว 1 เมตร
    และมีความสูง แตกต่างกันไป ซึ่งกำแพงเมืองไทยจะมีทั้งหมด N ส่วน
    แต่ละส่วนมีความสูง Hi เมตร (1 ≤ i ≤ N) 

    
    ความสูงของอิฐมีหลายขนาด สูงเท่าไหร่ก็ได้ตั้งแต่ 1 - 1,000,000,000
    กว้างได้แค่ 1 เมตรเท่านั้น (เท่ากับความกว้าง 1 ส่วนของกำแพงพอดี)
    *อิฐ 1 ก้อนจะมีความกว้าง 1 เมตร

    input
        บรรทัดแรกรับจำนวนส่วนของของกำแพง N 
    

"""
from math import gcd
# ส่วนของกำแพงจำนวน N
input()
# ส่วนของความสูงของ ส่วนที่ i 
H_i = [int(i) for i in input().split()]

# ขนาดความสูงของอิฐที่น้อยที่สุด
size_of_high = gcd(*H_i)
sum_of_n = [v // size_of_high for v in H_i]
print(sum(sum_of_n))

