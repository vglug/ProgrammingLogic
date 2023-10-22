# Open the source file in read mode
source_file = open("source.txt", "r")

# Open the target file in append mode
target_file = open("target.txt", "a")

# Read the content from the source file
content = source_file.read()

# Append the content to the target file
target_file.write(content)

# Close both files
source_file.close()
target_file.close()

print("Content appended successfully.")
