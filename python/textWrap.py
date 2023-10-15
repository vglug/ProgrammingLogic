""" Text wrap """
import textwrap

input_str = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
line_width = 4

# Use textwrap to wrap the input string
wrapped_text = textwrap.wrap(input_str, width=line_width)

# Print the wrapped text
for line in wrapped_text:
    print(line)
