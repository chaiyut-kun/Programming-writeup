seven = []
for k in range(9):
    seven.append(int(input()))
summit = sum(seven)
result = summit-100
unknow = []

for i in range(len(seven)):
    for j in range(i,len(seven)):
        if seven[i] + seven[j] == result:
            unknow.append([seven[i],seven[j]])



unknow = unknow[0]
show = [seven.remove(i) for i in unknow]
for i in seven:
    print(i)