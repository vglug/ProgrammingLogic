def remove_substring(main_string, substring):
    result = main_string.replace(substring, '')
    return result

# Example usage
original_string = "Hello, World! Hello, Python!"
substring_to_remove = "Hello, "
modified_string = remove_substring(original_string, substring_to_remove)

print(f"Original String: {original_string}")
print(f"Modified String: {modified_string}")
