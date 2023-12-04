# รับค่าของจำนวนข้อสอบ 
n = int(input())
# รับค่าเฉลยคำตอบ
True_answer = input()


# function slicing
slicing = lambda  x : x[:n] 

#default team 
team = {'Adrian':['ABC'*n,0] , 'Bruno' : ['BABC'*n,0] , 'Goran' : ['CCAABB'*n,0]}

# KEY = NAME : VALUES -> V0 = PATTERN , V1 = POINT OF EACH
map_team = {k : [slicing(v[0]),v[1]] for k , v in team.items()}


max_point = 0

for name , values in map_team.items():
    
    # Check answer
    for answer in range(n):
        if values[0][answer] == True_answer[answer]:
            values[1]+=1
            
    # find MAXPOINT 
    if values[1] > max_point :
        max_point = values[1]

def find_max(val : dict):
    print(val)
    

find_winner = {key : values for key, values in map_team.items() if values[1] == max_point }
# find_winner2 = dict(filter(find_max , map_team))



print(max_point , *(find_winner.keys()) ,sep='\n')

