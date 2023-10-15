def armstrong(n):
    #converting the number to string to count the number og digits
    n_str = str(n)
    n_digits = len(n_str)
    # intialize the variable to store 
    arm_num = 0
    
    # calculate the armstrong number ABC= An+Bn+Cn
    for digit in n_str:
        arm_num += int(digit) ** n_digits
    
    return arm_num == n
#input
num = int(input('Enter the number:'))
#checking
if armstrong(num):
    print(f'{num} is an armstrong number')
else:
    print(f'{num} is not an armstrong number')