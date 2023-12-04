seven_dwarves = [int(input()) for _ in range(9)]
Sum_seven = sum(seven_dwarves)
unknow = [[seven_dwarves[i] , seven_dwarves[j]] for i in range(9) for j in range(9) if seven_dwarves[i] + seven_dwarves[j] == Sum_seven-100 ][0]
remove_unknown = [seven_dwarves.remove(i) for i in unknow]
print(*seven_dwarves , sep="\n")
