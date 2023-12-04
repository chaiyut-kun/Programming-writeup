import re

prototype = input("")
upper = prototype.upper()
lower = prototype.lower()

if prototype == upper:
    print("All Capital Letter")

elif prototype  == lower:
    print("All Small Letter")
else:
    print("Mix")


""" 

    หากทุกข้อความเป็น ตัวพิมพ์ใหญ่ก็จะแสดง All Capital Letter
    หากทุกข้อความเป็น ตัวพิมพ์เล็กจะแสดง   All Small Letter

"""