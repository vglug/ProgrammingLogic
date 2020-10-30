import re

textfile = open(filename, 'r')
filetext = textfile.read()
textfile.close()
matches = re.findall("(<(\d{4,5})>)?", filetext)

