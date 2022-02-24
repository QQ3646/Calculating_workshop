# Алгоритм на вход требует симметрическую положительно-определенную матрицу на вход!

import math  # Для различных математических констант/простейших функций

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

matrix = []
bVector = []

size = int(input())
# Вариант, использующий задание формулой
# for i in range(size):
# matrix.append([0] * size)
#     for j in range(size):
#         matrix[i][j] = ?

 # Вариант со вводом матриц руками
for i in range(size):
    ipt = input()
    matrix.append(list(map(float, ipt.split()[:-1])))
    bVector.append(float(ipt.split()[-1]))

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

yVector = [0] * size
for i in range(size):
    for j in range(i):
        bVector[i] -= lm[i][j] * yVector[j]
    yVector[i] = bVector[i] / lm[i][i]
transposition(lm)


xVector = [0] * size
for i in reversed(range(size)):
    for j in reversed(range(i + 1, size)):
        yVector[i] -= lm[i][j] * xVector[j]
    xVector[i] = yVector[i] / lm[i][i]

print("\n".join(map(str, xVector)))