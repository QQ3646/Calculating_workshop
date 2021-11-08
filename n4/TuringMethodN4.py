import math  # Для различных математических констант/простейших функций
from someStuff.someMethods import matrix_input, gauss_method

def MatrixMulti(matrix1, matrix2):
    cpy = []
    for i in range(len(matrix1)):
        cpy.append([0] * len(matrix2[i]))
        for j in range(len(matrix2[i])):
            cpy[i][j] = sum(matrix1[i][n] * matrix2[n][j] for n in range(len(matrix2)))
    return cpy

def transposition(matrix):
    for i in range(size):
        for j in range(i + 1, size):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

mode = 0
# 0 для считывания с файла input.txt и вывод в файл output.txt
# 1 для считывания и вывода в консоль

matrix = []
bVector = []
size = matrix_input(matrix, bVector, mode)

resultT = []
for i in range(size):
    resultT.append([0] * size)
    resultT[i][i] = 1
for k in range(size):
    for i in range(k + 1, size):
        c = matrix[k][k] / math.sqrt(matrix[k][k] ** 2 + matrix[i][k] ** 2)
        s = matrix[i][k] / math.sqrt(matrix[k][k] ** 2 + matrix[i][k] ** 2)
        for j in range(k, size):
            matrix[k][j], matrix[i][j] = c * matrix[k][j] + s * matrix[i][j], -s * matrix[k][j] + c * matrix[i][j]
        bVector[k], bVector[i] = c * bVector[k] + s * bVector[i], -s * bVector[k] + c * bVector[i]
        T = []
        for j in range(size):
            T.append([0] * size)
            T[j][j] = 1
        T[k][k], T[i][i] = c, c
        T[k][i], T[i][k] = s, -s
        resultT = MatrixMulti(T, resultT)
xVector, _ = gauss_method(size, matrix, bVector)

# for i in range(0, size):
#     for j in range(0, size):
#         print(str(list(matrix)[i][j]), end=" ")
#     print("")
print("\n".join(map(str, xVector)))
transposition(resultT)
check = MatrixMulti(resultT, matrix)
for i in range(size):
    print(" ".join(str(check[i][j]) for j in range(size)))