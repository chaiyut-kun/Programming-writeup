x , y = [int(i) for i in input().split()]
print(f"{int(y/x if y%x==0 else y/x+1) if y>=x else 2}")
