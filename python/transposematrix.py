"""This gives the transpose of a matrix"""
def transpose_matrix(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed

r=int(input('Enter no. of row:'))
c=int(input('Enter no. of column:'))
matrix=[[int(input())for x in range(c)] for y in range(r)]

transposed_matrix = transpose_matrix(matrix)
print(transposed_matrix)
