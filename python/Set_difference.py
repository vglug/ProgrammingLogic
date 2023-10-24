def find_set_difference(a, b):
    set_difference = set(a) - set(b)
    return (set_difference)
a=[2,3,4,9]
b=[1,5,6,7,8]
result = find_set_difference(a,b)
print(result)