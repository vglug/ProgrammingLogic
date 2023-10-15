def nearest_to_average(lst):
    avg = sum(lst) / len(lst)
    return min(lst, key=lambda x: abs(x - avg))

# Example usage
my_list = [1, 5, 9, 2, 3, 7]
result = nearest_to_average(my_list)
print(f"The element nearest to the average is: {result}")
