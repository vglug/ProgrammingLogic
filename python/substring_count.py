def count_substring_occurrences(substring, original_string):
    count = 0
    substring_length = len(substring)

    for i in range(len(original_string) - substring_length + 1):
        if original_string[i:i+substring_length] == substring:
            count += 1

    return count

substring = "ab"
original_string = "ababaababa"

print(count_substring_occurrences(substring, original_string)) 