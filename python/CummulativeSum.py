"""  Program to find a cumulative sum of the list """
input_list = [10, 20, 30, 40, 50]
cumulative_sum = []

total = 0
for num in input_list:
    total += num
    cumulative_sum.append(total)

print(cumulative_sum)
