def replace_first_vowel_with_dash(input_string):
    vowels = "AEIOUaeiou"
    for char in input_string:
        if char in vowels:
            return input_string.replace(char, '-', 1)
    return input_string


input_string = "Hello, world!"
result = replace_first_vowel_with_dash(input_string)
print(result)
