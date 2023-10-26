"""SWAP TWO STRING"""
def swap_elements(lst, index1, index2):
    """Swap elements at index1 and index2 in the given list."""
    if 0 <= index1 < len(lst) and 0 <= index2 < len(lst):
        lst[index1], lst[index2] = lst[index2], lst[index1]
my_list = [1, 2, 3, 4, 5]
index_to_swap1 = 1
index_to_swap2 = 3

print("Original List:", my_list)

# Swap elements at index1 and index2
swap_elements(my_list, index_to_swap1, index_to_swap2)

print("List after swapping elements at index {} and {}: {}".format(index_to_swap1, index_to_swap2, my_list))
