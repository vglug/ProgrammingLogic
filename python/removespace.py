""" Remove space from string without built in function"""
def remove_spaces(input_string):
    output_string = ""
    for char in input_string:
        if char != " ":
            output_string += char
    return output_string

input_string = input("Enter string:")
result = remove_spaces(input_string)
print(result)
