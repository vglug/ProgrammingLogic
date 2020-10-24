""" Palindrom or not given string """

# function which return reverse of a string
def isPalindrome(s):
    return s == s[::-1]
 
 
# Getting string from user
s = input("Enter word: ")
ans = isPalindrome(s)

# Checking the given string same as reversed string then print "Yes". otherwise print "No"
if ans:
    print("Yes")
else:
    print("No")
