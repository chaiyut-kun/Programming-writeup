m,n = [int(i) for i in input().split()]
List = []

# M=m
# while m>0: #column
List = [[int(i) for i in input().split()] for _ in range(m)]
    # m-=1
    # templist = []
    
# while m < M:
#     templist = [int(i) for i in input().split()]
#     List[m] = [List[m][i] + templist[i] for i in range( len( List[m] ) ) ]
#     m+=1


for i in range(len(List)):
    temp = " ".join([str(i) for i in List[i]])
    print(temp)
