check_list =["F" if i % 2 == 0 and i != 2 else "T" for i in [int(input()) for _ in range(int(input()))] ]
print(*check_list , sep="\n")