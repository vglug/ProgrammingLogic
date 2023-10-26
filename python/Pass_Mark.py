a=[]
b = ["Tamil", "English", "Maths", "Science", "Social"]
for subject in b:
    mark = int(input(f"Enter Your Mark for {subject}: "))
    a.append(mark)
if a[0]>=35:
    print("Tamil: Pass")
else:
    print("Tamil: Fail")
if a[1]>=35:
    print("English: Pass")
else:
    print("English: Fail")

if a[2]>=35:
    print("Maths: Pass")
else:
    print("Maths: Fail")
if a[3]>=35:
    print("Science: Pass")
else:
    print("Science: Fail")
if a[4]>=35:
    print("Social: Pass")
else:
    print("Social: Fail")