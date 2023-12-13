from math import lcm

input()
# จำนวนรถเมล์
Bus_n = [int(i) for i in input().split()]
Timing = lcm(*Bus_n)
print(Timing)