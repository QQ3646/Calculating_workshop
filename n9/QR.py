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
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    return matrix

def findQR(m, size):
    resultT = []
    for i in range(size):
        resultT.append([0] * size)
        resultT[i][i] = 1
    matrix = []
    for i in range(len(m)):
        matrix.append(m[i][:])
    for k in range(size):
        for i in range(k + 1, size):
            c = matrix[k][k] / math.sqrt(matrix[k][k] ** 2 + matrix[i][k] ** 2)
            s = matrix[i][k] / math.sqrt(matrix[k][k] ** 2 + matrix[i][k] ** 2)
            for j in range(k, size):
                matrix[k][j], matrix[i][j] = c * matrix[k][j] + s * matrix[i][j], -s * matrix[k][j] + c * matrix[i][j]
            T = []
            for j in range(size):
                T.append([0] * size)
                T[j][j] = 1
            T[k][k], T[i][i] = c, c
            T[k][i], T[i][k] = s, -s
            resultT = MatrixMulti(T, resultT)
    return transposition(resultT), matrix

def iteration(matrix, size):
    cpy = []
    for i in range(len(matrix)):
        cpy.append(matrix[i][:])
    q, r = findQR(matrix, size)
    # newA = MatrixMulti(makeReverse(q), cpy)
    # newA = MatrixMulti(newA, q)
    return MatrixMulti(r, q)

def qralg(matrix, size):
    while True:
        diag = True
        for i in range(size):
            if not diag:
                break
            for j in range(i):
                if abs(matrix[i][j]) > 10e-10:
                    diag = False
        if diag:
            break
        else:
            matrix = iteration(matrix, size)
    return [matrix[i][i] for i in range(size)]

if __name__ == "__main__":
    mode = 0
    # 0 для считывания с файла input.txt и вывод в файл output.txt
    # 1 для считывания и вывода в консоль

    matrix = []
    bVector = []
    size = matrix_input(matrix, bVector, mode)

    lambdes = qralg(matrix, size)
    for i, elem in enumerate(lambdes):
        print(f"{i + 1} lambda:")
        print(elem)
