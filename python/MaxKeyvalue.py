my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}

max_key = max(my_dict, key=my_dict.get)

print("Key with maximum value:", max_key)
