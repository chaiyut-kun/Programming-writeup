def bubble_sort(arr):
    n = len(arr)

    # ผ่านไปทุกรอบ
    for i in range(n):
        # ลูปในเซตที่ยังไม่ถูกเรียง
        for j in range(0, n-i-1):
            # เปรียบเทียบสมาชิกที่ตำแหน่ง j กับ j+1
            print(f"{i = }  {j = }",end="   ")
            if arr[j] > arr[j+1]:
                # สลับค่าถ้าตำแหน่ง j มีค่ามากกว่าตำแหน่ง j+1
                arr[j], arr[j+1] = arr[j+1], arr[j]

# ตัวอย่างการใช้งาน
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)

print("ลิสต์ที่เรียงลำดับแล้ว:", my_list)
