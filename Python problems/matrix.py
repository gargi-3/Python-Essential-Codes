matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Elements of matrix 1: ")
print(matrix[0][0], " ", matrix[0][1], " ", matrix[0][2])
print(matrix[1][0], " ", matrix[1][1], " ", matrix[1][2])
print(matrix[2][0], " ", matrix[2][1], " ", matrix[2][2])

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("Elements of matrix 2: ")
print(matrix2[0][0], " ", matrix2[0][1], " ", matrix2[0][2])
print(matrix2[1][0], " ", matrix2[1][1], " ", matrix2[1][2])
print(matrix2[2][0], " ", matrix2[2][1], " ", matrix2[2][2])

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(matrix)):
    for j in range(len(matrix2)):
        result[i][j] = matrix[i][j] + matrix2[i][j]

print("Elements of Result matrix: ")
print(result[0][0], " ", result[0][1], " ", result[0][2])
print(result[1][0], " ", result[1][1], " ", result[1][2])
print(result[2][0], " ", result[2][1], " ", result[2][2])