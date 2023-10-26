x= input("Enter a string: ")
y= {}
for char in x:
    if char.isalpha(): 
        if char in y:
            y[char] += 1
        else:
            y[char] = 1
z = min(y, key=y.get)
print(f"The least frequent character is '{z}' with a frequency of {y[z]}.")
