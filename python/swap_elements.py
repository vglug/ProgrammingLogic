def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
my_list=[23,65,19,90]
swap(my_list, 0, 2)

print(my_list)