A, B, C = [int(i) for i in input().split()]
# สร้างรายการตำแหน่งของจิงโจ้
positions = sorted([A, B, C])

# จำนวนครั้งที่จิงโจ้สามารถกระโดดได้
jumps = 0

# ตรวจสอบที่ตำแหน่งของ A, B, C
while ( positions[0] + 1 != positions[1] ) or (positions[1] + 1 != positions[2]) :

    # กระโดดจิงโจ้ที่ตำแหน่งที่มีระยะทางมากที่สุดระหว่างตัวอื่น
    if positions[1] - positions[0] < positions[2] - positions[1]:
        positions[0] = positions[1] + 1
        print(f"{positions[0]     = }")
        print(f"{positions[1]     = }" )
        
    else:
        positions[2] = positions[1] - 1
        print(f"{positions[2]     = }")
        print(f"{positions[1] - 1 = }")


    # เรียงลำดับตำแหน่งอีกครั้งหลังจากกระโดด
    positions = sorted(positions)
    print(f"{positions        = }")
    print()
    jumps += 1

print(f"{jumps = }")