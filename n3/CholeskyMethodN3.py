# Алгоритм на вход требует симметрическую положительно-определенную матрицу на вход!

import math  # Для различных математических констант/простейших функций
from someStuff.someMethods import matrix_input, gauss_method


def transposition(matrix):
    for i in range(size):
        for j in range(i + 1, size):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

def sigmaII(end, matrix):
    sig_res = 0
    for i in range(end):
        sig_res += matrix[end][i]**2
    return sig_res


def sigmaJI(end, matrix, n):
    sig_res = 0
    for i in range(end):
        sig_res += matrix[end][i]*matrix[n][i]
    return sig_res


mode = 0
# 0 для считывания с файла input.txt и вывод в файл output.txt
# 1 для считывания и вывода в консоль

matrix = []
bVector = []
size = matrix_input(matrix, bVector, mode)

lm = [0] * size
for i in range(size):
    lm[i] = list([0] * size)

lm[0][0] = math.sqrt(matrix[0][0])
for i in range(1, size):
    lm[i][0] = matrix[i][0] / lm[0][0]

for i in range(1, size):
    lm[i][i] = math.sqrt(matrix[i][i] - sigmaII(i, lm))
    for j in range(i + 1, size):
        lm[j][i] = (matrix[j][i] - sigmaJI(i, lm, j)) / lm[i][i]

yVector, _ = gauss_method(size, lm, bVector)
transposition(lm)

xVector, _ = gauss_method(size, lm, yVector)

print("\n".join(map(str, xVector)))