""" 

    s = average value
    x1 = first value 
    x2 = second value 

    s = (x1+x2)/2
    10 = (10+x2)/2 
    20 = 10+x2
    10 = x2

    
"""

# x1,x2 = map(int,input().split())
# s = (x1+x2)/2
# print(s)

x1,s = map(float,input().split())
x2 = (s*2)-x1
print(int(x2))