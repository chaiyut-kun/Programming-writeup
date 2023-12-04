# ผู้เข้าแข่งขัน
Contestants = {1:[],2:[],3:[],4:[],5:[]}
Max = 0
for k , v in Contestants.items():
    point = list(map( int , input().split() ) )
    v.extend(point)
    if sum(v) > Max :    Max = sum(v)

find_winner = {k : sum(v) for k , v in Contestants.items() if sum(v) == Max}
print(*find_winner.keys(), *find_winner.values(),sep=" ")