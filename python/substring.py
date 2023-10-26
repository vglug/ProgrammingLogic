"""REMOVE ALL SUBSTRING"""
def remove_substring(input_string, substring):
    result = input_string.replace(substring, '')
    return result
original_string = "Hello, World! Hello, Universe!"
substring_to_remove = "Hello, "
result_string = remove_substring(original_string, substring_to_remove)

print("Original String:", original_string)
print("Result String:", result_string)
