def is_perfect_number(number):
    if number <= 0:
        return False

    divisors = [1]  
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.extend([i, number // i])

    return sum(divisors) == number
num = int(input("Enter a number: "))
if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
