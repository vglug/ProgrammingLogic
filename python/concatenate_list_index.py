list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

concatenated_list = [f'{a}{b}' for a, b in zip(list1, list2)]

print(concatenated_list)
