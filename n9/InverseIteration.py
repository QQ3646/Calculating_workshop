import math  # Для различных математических констант/простейших функций
from someStuff.someMethods import matrix_input, gauss_method
from random import randint
from QR import qralg

def norm(v):
    return max(abs(v[i]) for i in range(len(v)))


def normalize(v):
    v1 = v[:]
    norma = (sum(v[i] ** 2 for i in range(len(v)))) ** 0.5
    for i in range(len(v1)):
        v1[i] /= norma
    return v1


def makeEMatrix(size):
    res = []
    for i in range(size):
        res.append([0] * size)
        res[i][i] = 1
    return res


def MatrixMulti(matrix1, matrix2):
    cpy = []
    for i in range(len(matrix1)):
        cpy.append([0] * len(matrix2[i]))
        for j in range(len(matrix2[i])):
            cpy[i][j] = sum(matrix1[i][n] * matrix2[n][j] for n in range(len(matrix2)))
    return cpy


def MatrixScalarMulti(matrix1, const):
    cpy = []
    for i in range(len(matrix1)):
        cpy.append([0] * len(matrix1[i]))
        for j in range(len(cpy[i])):
            cpy[i][j] = matrix1[i][j] * const
    return cpy

def MatrixMinusMatrix(matrix1, matrix2):
    cpy = []
    for i in range(len(matrix1)):
        cpy.append([0] * len(matrix1[i]))
        for j in range(len(cpy[i])):
            cpy[i][j] = matrix1[i][j] - matrix2[i][j]
    return cpy

def scalar(v1, v2):
    return sum(v1[i] * v2[i] for i in range(len(v1)))


mode = 0
# 0 для считывания с файла input.txt и вывод в файл output.txt
# 1 для считывания и вывода в консоль

matrix = []
bVector = []
size = matrix_input(matrix, bVector, mode)

eps = 10e-6

countOfIter = 10

# currVector = list([randint(-100, 100)] for _ in range(size))
currVector = [1, 1, 1]
prevVector = currVector[:]

sigma = qralg(matrix, size)
finalVect = []
# sigma = [-7.87279]
for i in sigma:
    while True:
        currVector, _ = gauss_method(size, MatrixMinusMatrix(matrix, MatrixScalarMulti(makeEMatrix(size), i)), prevVector)
        currVector = normalize(currVector)
        if abs(norm(currVector) - norm(prevVector)) < eps:
            prevVector = normalize(currVector)
            break
        prevVector = currVector[:]
    finalVect.append(prevVector)
for i in range(len(sigma)):
    cpyCurr = [[finalVect[i][j]] for j in range(size)]
    check = MatrixMulti(matrix, cpyCurr)
    print(f"lambda {i + 1} = {sigma[i]}\n" + "\n".join(str(finalVect[i][j]) for j in range(size)))
    print("\ncheck:\n" + "\n".join(str(check[j][0]) + f" / {sigma[i]} = {check[j][0] / sigma[i]}" for j in range(size)))
