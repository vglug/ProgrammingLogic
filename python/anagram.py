word1 = input('enter the word:')
word2 = input(' enter the 2nd word:')
Lword1 = word1.lower()
Lword2 = word2.lower()

if sorted(Lword1)==sorted(Lword2):
    print(f'{word1} and {word2} are anagram')
else:
    print('this is not a anagram')