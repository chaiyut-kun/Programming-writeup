ans = set() #สร้างเซตเพื่อป้องกันไม่ให้จำนวนซ้ำกัน
m = 1
while m<=10:
    ans.add(int(input()) % 42)
    m+=1
print(len(ans))