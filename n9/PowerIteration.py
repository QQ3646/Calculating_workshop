# Если |sigma1| > |sigma2| >= |sigma3| >= ... >= |sigmaM|
#            !  >  !

import math  # Для различных математических констант/простейших функций
from someStuff.someMethods import matrix_input, gauss_method
from decimal import *
from random import randint

def normalize(v):
    v1 = v[:]
    norm = (sum(v1[i][0]**2 for i in range(len(v1))))**0.5
    for i in range(len(v1)):
        v1[i][0] /= norm
    return v1

def MatrixMulti(matrix1, matrix2):
    cpy = []
    for i in range(len(matrix1)):
        cpy.append([0] * len(matrix2[i]))
        for j in range(len(matrix2[i])):
            cpy[i][j] = sum(matrix1[i][n] * matrix2[n][j] for n in range(len(matrix2)))
    return cpy


def scalar(v1, v2):
    return sum(v1[i][0] * v2[i][0] for i in range(len(v1)))


mode = 0
# 0 для считывания с файла input.txt и вывод в файл output.txt
# 1 для считывания и вывода в консоль

matrix = []
bVector = []
size = matrix_input(matrix, bVector, mode)

countOfIter = 10

# currVector = list([randint(-100, 100)] for _ in range(size))
currVector = [[1], [0], [0]]
sigma1 = 0
prevVector = currVector[:]
for i in range(countOfIter):
    currVector = MatrixMulti(matrix, prevVector)
    sigma1 = scalar(currVector, prevVector) / scalar(prevVector, prevVector)
    prevVector = normalize(currVector)
print(sigma1, "\n" + "\n".join(str(currVector[i][0]) for i in range(size)))
check = MatrixMulti(matrix, currVector)
print("\n" + "\n".join(str(check[i][0]) + f" / {sigma1} = {check[i][0] / sigma1}" for i in range(size)))