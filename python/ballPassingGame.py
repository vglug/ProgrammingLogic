''' Ball Passing Game '''
def passing(n, t):
    check = 1
    val = 1

    for i in range(t):
        if check == 1:
            if val + 1 == n:
                check = -1
            val += 1
        else:
            if val - 1 == 1:
                check = 1
            val -= 1

    return val

n = int(input("Enter the Number of members: "))
t = int(input("Enter the seconds: "))
result = passing(n, t)
print("The person holding the pillow after", t, "seconds is:", result)
