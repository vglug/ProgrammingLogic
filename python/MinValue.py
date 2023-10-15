my_dict = {'a': 5, 'b': 3, 'c': 8, 'd': 1}

min_key = min(my_dict, key=my_dict.get)
print(min_key)
