from collections import Counter

# จำนวนข้อมูลที่ user จะป้อนเข้ามา
input()
data_list = [int(i) for i in input().split()]
counter_value = dict(Counter(data_list))
most_count_values = max([v for k , v in counter_value.items()])
list_values = sorted([k for k, v in counter_value.items() if v == most_count_values])
print(*list_values,sep=" ")

