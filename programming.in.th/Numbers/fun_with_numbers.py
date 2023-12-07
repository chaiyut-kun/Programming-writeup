# asset

n_of_order = int(input())
numbers = sorted([int(i)  for i in input().split()] )


min_value_not_zero = max(numbers)
for i in numbers :
    if i != 0 :
        if i < min_value_not_zero:
            min_value_not_zero = i

#  end asset

# algorithm 1 
numbers.remove(min_value_not_zero)
numbers.insert(0 , min_value_not_zero)
print(*numbers , sep="")

# algorithm is Success !

        
#  algorithm 2
index_min_value = numbers.index(min_value_not_zero)
numbers[0] , numbers[index_min_value] = numbers[index_min_value] , numbers[0]
print(*numbers, sep="")

# algorithm 2 is Success !!