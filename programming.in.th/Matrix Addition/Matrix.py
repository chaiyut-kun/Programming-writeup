""" 
    column input m
    row input n
    matrix = m*n dimension
    loop = m+1 round for get input value in array
    
 """

m,n = map(int,input().split())
List = []

M=m
while m>0: #column
    templist = list(int(i) for i in input().split())
    List.append(templist)
    m-=1
    templist = []
    
while m < M:
    templist = list(int(i) for i in input().split())
    List[m] = [List[m][i] + templist[i] for i in range(len(List[m]))]
    m+=1


for i in range(len(List)):
    temp = " ".join([str(i) for i in List[i]])
    print(temp)


