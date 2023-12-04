from icecream import ic

n = int(input()) # จำนวนข้อสอบ
True_answer = input() # คำตอบทั้งหมด

team = ['Adrian', 'Bruno', 'Goran']

# แพทเทิร์นการเดาข้อสอบของแต่ละคน
slicing = lambda x : x[:n]
answer_list = list(map(slicing,[('ABC'*n), ('BABC'*n), ('CCAABB'*n)]))
print(answer_list)


# point of Adrian , Bruno , Goran
# count_point_each = [0]*3

# for index, pattern in enumerate(answer_list):
#     for index_answer in range(n):
#         if pattern[index_answer] == answer[index_answer]:
#             count_point_each[index] += 1
            

# max_count = max(count_point_each)

# for i, c in enumerate(count_point_each):
#     if c == max_count:
#         print(person[i])