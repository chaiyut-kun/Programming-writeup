char = ["A","B","C"]
my_list = ["ball", " ", " "]
code = input()
for i in code:
    if char.index(i) + 1 <= 2:
        my_list[char.index(i)], my_list[char.index(i) + 1] = my_list[char.index(i) + 1], my_list[char.index(i)]
    else:
        my_list[char.index(i)], my_list[0] = my_list[0], my_list[char.index(i)]

print(my_list.index("ball") + 1)