def find_lcm(x, y):
    # Find the greater of the two numbers
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1

    return lcm

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = find_lcm(num1, num2)
print(f"The L.C.M. of {num1} and {num2} is {result}")
