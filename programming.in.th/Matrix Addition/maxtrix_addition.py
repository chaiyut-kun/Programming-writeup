m,n = [int(i) for i in input().split()]
Matrix = [[int(col) for col in input().split()] for _ in range(m)]
Adder = [[int(col) for col in input().split()] for _ in range(m)]
result = [[sum(m) for m  in zip(M , A)] for M , A in zip(Matrix , Adder) ]

print("\n".join([' '.join(map(str , res)) for res in result]))    