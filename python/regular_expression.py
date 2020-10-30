import re
#open text file
textfile = open(filename, 'r')
#read the file
filetext = textfile.read()
#when file opened the file should be closed
textfile.close()
matches = re.findall("(<(\d{4,5})>)?", filetext)

