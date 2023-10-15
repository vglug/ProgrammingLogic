def capitalize_words_in_file(doc.txt):
    try:
        with open(doc.txt, 'r') as file:
            content = file.read()
            
        capitalized_content = ' '.join(word.capitalize() for word in content.split())
        
        with open(doc.txt ,'w') as file:
            file.write(capitalized_content)
            
        print(f'Capitalized the first letter of each word in {doc.txt }')
    except FileNotFoundError:
        print(f'File not found: {doc.txt}')

doc.txt = 'vikki.txt'  
capitalize_words_in_file( doc.txt )
