""" Pass By Value """
def add100(num):
    num+=100
    print("Changed value: "+str(num))

print("-------Pass By value-------")
num = int(input("Enter the number: "))
add100(num)
print("Input after the Function calls: "+str(num))