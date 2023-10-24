def replace_first_vowel(string):
    vowels = 'aeiou'
    
    for char in string:
        if char.lower() in vowels:
            return string[:string.index(char)] + '-' + string[string.index(char) + 1:]
            
    return string

string = "hello world"
print(replace_first_vowel(string)) 