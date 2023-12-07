from collections import Counter

# จำนวนข้อมูลที่ user จะป้อนเข้ามา
n = int(input())
data_list = [int(i) for i in input().split()]

most_count = Counter(data_list).most_common()[0][1]
def check_value(item : tuple):
    if  item[1] == most_count:
        return item[0]
filter_count = dict( filter(check_value , dict(Counter(data_list)).items() ) )
print(*sorted(filter_count.keys()) , sep=" ")



