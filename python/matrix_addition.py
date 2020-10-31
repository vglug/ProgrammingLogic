#Using for loop
A = [[10,12,13],
     [1,4,5],
     [6,9,0]]
B = [[3,5,5],
     [5,1,1],
     [0,4,6]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
#Iterate through rows
for i in range(len(A)):
    #Iterate through collumns
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]
for r in result:
    print(r)

#Using nested list comprehension
A = [[10,12,13],
     [1,4,5],
     [6,9,0]]
B = [[3,5,5],
     [5,1,1],
     [0,4,6]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
for r in result:
    print(r)

#Using Zip() and Sum
A = [[10,12,13],
     [1,4,5],
     [6,9,0]]
B = [[3,5,5],
     [5,1,1],
     [0,4,6]]
result = [map(sum, zip(*t)) for t in zip(A, B)] 
print(result)
