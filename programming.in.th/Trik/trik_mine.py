""" 
    1 2 3
    A B C

input = A
result = A+1
output = 2

input = C+1 = 4 
if C+1 > 3 :
    output = 1


""" 


# import time 

# def timing(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         time_result = time.time() - start
#         print(time_result)
#         return result
#     return wrapper
    
# @timing
def program():
    char = ["A","B","C"]
    my_list = ["ball", " ", " "]
    code = input()
    for i in code:
        if char.index(i) + 1 <= 2:
            my_list[char.index(i)], my_list[char.index(i) + 1] = my_list[char.index(i) + 1], my_list[char.index(i)]
        else:
            my_list[char.index(i)], my_list[0] = my_list[0], my_list[char.index(i)]

    return my_list.index("ball") + 1

# print(program())



char = ["A","B","C"]
my_list = ["ball", " ", " "]
code = input()
for i in code:
    if char.index(i) + 1 <= 2:
        my_list[char.index(i)], my_list[char.index(i) + 1] = my_list[char.index(i) + 1], my_list[char.index(i)]
    else:
        my_list[char.index(i)], my_list[0] = my_list[0], my_list[char.index(i)]

print(my_list.index("ball") + 1)