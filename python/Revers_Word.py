def reverse_words_in_string(input_string):
    words = input_string.split()
    reversed_words = words[::-1]
    reversed_string = ' '.join(reversed_words)

    return reversed_string
input_string = "Hello World"
result = reverse_words_in_string(input_string)
print(result)  
