list = [[3,1],[4,2],[10,1],[1,2],[4,1],[1,1],[5,1],[7,1],[2,1],[46,1]]

for main in range(len(list)):
    for sec in range(len(list)):
        if main == sec:
            continue
        if list[main][0] > list[sec][0]:
            continue
        elif list[main][0] < list[sec][0]:
            list[main] , list[sec] = list[sec] , list[main]
        elif list[main][0] == list[sec][0]:
            if list[main][1] < list[sec][1]:
                list[main] , list[sec] = list[sec] , list[main]
            else:
                continue
            

# print(list)


list = [3,4,10,1,4,1,5,7,2,46]

for main in range(len(list)):
    for sec in range(len(list)):
        if main == sec:
            continue
        if list[main] > list[sec]:
            continue
        elif list[main] < list[sec]:
            list[main] , list[sec] = list[sec] , list[main]
        elif list[main] == list[sec]:
            continue
            

print(list)

w