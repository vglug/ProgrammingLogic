def slice_list(lst, n):
    avg = len(lst) // n
    remainder = len(lst) % n
    start = 0
    for i in range(n):
        end = start + avg + (1 if i < remainder else 0)
        sublist = lst[start:end]
        print(f"Sublist {i + 1}: {sublist}")
        start = end

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_sublists = 3
slice_list(my_list, num_sublists)
