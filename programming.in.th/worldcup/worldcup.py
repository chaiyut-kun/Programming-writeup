Teams = [[ input() , [] ] for _ in range(4)]
raw_score = [[int(i) for i in input().split()] for _ in range(4)]


for tm in range(4):
    for competitor in  range(4):
        if tm == competitor:
            Teams[tm][1].append(0)
        
        elif raw_score[tm][competitor] > raw_score[competitor][tm]:
            Teams[tm][1].append(3)
           
        elif raw_score[tm][competitor] < raw_score[competitor][tm] :
            Teams[tm][1].append(0)
            
        elif raw_score[tm][competitor] == raw_score[competitor][tm] :
            Teams[tm][1].append(1)
            
        
   

process_teams = [tm[0] for tm in Teams ]
process_point = [sum(tm[1]) for  tm in Teams ]

all_list = [[process_teams[i] , process_point[i] , sum(raw_score[i])] for i in range(4)]


# sorting 
for main in range(4):
    for sec in range(4):
        if main == sec :
            continue
            
        if all_list[main][1] < all_list[sec][1]:
            continue
        
        elif all_list[main][1] > all_list[sec][1]:
            all_list[main] , all_list[sec] = all_list[sec] , all_list[main]

        elif all_list[main][1] == all_list[sec][1] :
            if all_list[main][2] > all_list[sec][2] :
                all_list[main] , all_list[sec] = all_list[sec] , all_list[main]
            else:
                continue

            
for i in (all_list):
    print(i[0],i[1],sep=" ")