round = int(input())
numlist = []
while round >0:
    numlist.append(int(input()))
    round-=1

print(f"{min(numlist)}\n{max(numlist)}")