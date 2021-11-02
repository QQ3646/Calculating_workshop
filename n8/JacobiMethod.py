# Только симметрические матрицы
import math  # Для различных математических констант/простейших функций
from someStuff.someMethods import matrix_input, gauss_method
from decimal import *

J = []

def make0Matrix(size):
    res = []
    for i in range(size):
        res.append([0] * size)
    return res


def transpos(m1):
    res = []
    for i in range(len(m1)):
        res.append(m1[i][:])
    for i in range(len(res)):
        for j in range(i):
            res[i][j], res[j][i] = res[j][i], res[i][j]
    return res


def matrixMul(m1, m2):
    res = make0Matrix(len(m1))
    # m2t = transpos(m2)
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            res[i][j] = sum(m1[i][m] * m2[m][j] for m in range(len(m1)))
    return res


def rotation(matrix):
    maxO = -math.inf
    p, q = 0, 0
    eq = False
    for i in range(size):
        for j in range(i):
            if abs(matrix[i][j]) > maxO:
                maxO = abs(matrix[i][j])
                p, q = i, j
                eq = False
                if Decimal(matrix[p][p]).quantize(Decimal("1.000000")).compare(
                        Decimal(matrix[q][q]).quantize(Decimal("1.000000"))) == Decimal('0'):
                    eq = True
            elif abs(matrix[i][j]) == maxO and not eq and matrix[i][i] == matrix[j][j]:
                p, q = i, j
                eq = True
    J1 = make0Matrix(size)
    for i in range(size):
        if i != p and i != q:
            J1[i][i] = 1
    if eq:
        angle = math.pi / 4
    else:
        fi = 2*matrix[p][q] / (matrix[q][q] - matrix[p][p])
        angle = math.atan(fi) / 2
    J1[p][p] = math.cos(angle)
    J1[q][q] = math.cos(angle)
    J1[p][q] = math.sin(angle)
    J1[q][p] = -math.sin(angle)
    J.append(J1)
    return matrixMul(matrixMul(transpos(J1), matrix), J1)


mode = 0
# 0 для считывания с файла input.txt и вывод в файл output.txt
# 1 для считывания и вывода в консоль

matrix = []
bVector = []
size = matrix_input(matrix, bVector, mode)

while True:
    diag = True
    for i in range(size):
        if not diag:
            break
        for j in range(i):
            if not Decimal(matrix[i][j]).quantize(Decimal("1.000000000000")).is_zero():
                matrix = rotation(matrix)
                diag = False
    if diag:
        break
eigenv = make0Matrix(size)
for i in range(size):
    eigenv[i][i] = 1
for i in J:
    eigenv = matrixMul(eigenv, i)
for i in range(size):
    print(f"{i + 1} lambda:")
    print(matrix[i][i])
    print("vector:")
    print(" ".join(list(str(eigenv[j][i]) for j in range(size))), "\n")

