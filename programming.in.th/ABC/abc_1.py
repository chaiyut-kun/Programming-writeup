
#  1
lnum = sorted([int(i) for i in input().split()])
# input abc character
order = input()
# หาว่า ตัวอักษรที่รับมาจาก order มันอยู่ตรงไหน ( index ไหน )
# indexOrder = [["A","B","C"].index(order[i]) for i in range(3)]

for i in ["A","B","C"]:
    # print(lnum[i],end=" ")
    print(lnum[ order.index(i) ] , end= " ")

# 2
lnum = sorted([int(i) for i in input().split()])
order = input()
for i in ["A","B","C"]:
    print(lnum[ order.index(i) ] , end= " ")



