def sum_of_diagonals(matrix):
    sum = 0
    n = len(matrix)
    for i in range(n):
        sum += matrix[i][i]
        sum += matrix[i][n-i-1]
    return sum

matrix = [
    [1, 4],
    [3, 10]
]
result= sum_of_diagonals(matrix)
print(result)