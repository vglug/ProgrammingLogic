def find_single_occurance_num(numbers):
    result =0
    for number in numbers:
        result^= number
    return result
numbers = [4,2,1,2,1]
single_occurance = find_single_occurance_num(numbers)
print(f'Single Occurance number in the list is {single_occurance}')