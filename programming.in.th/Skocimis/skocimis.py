posit = [int(i) for i in input().split()]

print(max(posit[2]-posit[1] , posit[1] - posit[0])-1)