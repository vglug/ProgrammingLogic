with open('file1.txt', 'r') as file:
    content = file.read()

with open('file2.txt', 'a') as file:
    file.write('\n')
    file.write(content)