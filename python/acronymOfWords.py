""" Check if a string is an Acronym of words """
def isAcronym(words, s):
    s = s.lower()
    acronym = ''.join(word[0] for word in words)
    return s == acronym

words = ["alice", "bob", "charlie"]
s = "abc"

result = isAcronym(words, s)
print(result)
