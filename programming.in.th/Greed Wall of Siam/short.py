from math import gcd
# ส่วนของกำแพงจำนวน N
input()
# ส่วนของความสูงของ ส่วนที่ i 
H_i = [int(i) for i in input().split()]
# ขนาดความสูงของอิฐที่น้อยที่สุด
size_of_high = gcd(*H_i)
print(sum([v // size_of_high for v in H_i]))