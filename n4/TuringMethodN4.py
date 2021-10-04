import math  # Для различных математических констант/простейших функций
from someStuff.someMethods import matrix_input, gauss_method

mode = 0
# 0 для считывания с файла input.txt и вывод в файл output.txt
# 1 для считывания и вывода в консоль

matrix = []
bVector = []
size = matrix_input(matrix, bVector, mode)
for k in range(size):
    for i in range(k + 1, size):
        c = matrix[k][k] / math.sqrt(matrix[k][k] ** 2 + matrix[i][k] ** 2)
        s = matrix[i][k] / math.sqrt(matrix[k][k] ** 2 + matrix[i][k] ** 2)
        for j in range(k, size):
            matrix[k][j], matrix[i][j] = c * matrix[k][j] + s * matrix[i][j], -s * matrix[k][j] + c * matrix[i][j]
        bVector[k], bVector[i] = c * bVector[k] + s * bVector[i], -s * bVector[k] + c * bVector[i]

xVector, _ = gauss_method(size, matrix, bVector)

# for i in range(0, size):
#     for j in range(0, size):
#         print(str(list(matrix)[i][j]), end=" ")
#     print("")
print("\n".join(map(str, xVector)))
