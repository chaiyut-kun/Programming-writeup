n = 5
# # True_answer = input()
# maxpoint = 5
# slicing = lambda  x : x[:n]
# team = {'Adrian':['ABC'*n,0] , 'Bruno' : ['BABC'*n,5] , 'Goran' : ['CCAABB'*n,0]}
# map_team = {k : [slicing(v[0]),v[1]] for k , v in team.items()}

# filtered = lambda x: dict(x).values()[1] == 5
# filter_team = dict( filter( filtered , map_team) )
# print(filter_team)

team = {
    'Adrian': ['ABC'*n, 0],
    'Bruno': ['BABC'*n, 5],
    'Goran': ['CCAABB'*n, 0]
}

# ฟังก์ชันที่ใช้ในการกรองค่า
def filter_by_value(item):
    print(filter_by_value)

# ใช้ฟังก์ชัน filter() เพื่อกรองค่า
filtered_team = dict(filter(filter_by_value, team.items()))

print(filtered_team)
