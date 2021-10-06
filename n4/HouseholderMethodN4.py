import math  # Для различных математических констант/простейших функций
from someStuff.someMethods import matrix_input, gauss_method


def sign(n):
    if n > 0:
        return 1
    return -1


def norm(n):
    sigma = 0
    for i in n:
        sigma += i ** 2
    return math.sqrt(sigma)


def Mmulti():
    pass


def CLmulti(a):
    b = []
    for i in range(len(a)):
        b.append([0] * len(a))
    for i in range(len(a)):
        for j in range(len(a)):
            b[i][j] = a[i] * a[j]
    return b


def matrixProd(size, amatrix, bmatrix):
    cpy = []
    for i in range(size):
        cpy.append([0] * size)
        for j in range(size):
            tempSum = 0
            for k in range(size):
                tempSum += amatrix[i][k] * bmatrix[k][j]
            cpy[i][j] = tempSum
    return cpy


def MCmulti(amatrix, bVector):
    cpy = []
    for i in range(len(amatrix)):
        temp = 0
        for j in range(len(amatrix)):
            temp += amatrix[i][j] * bVector[j]
        cpy.append(temp)
    return cpy


mode = 0
# 0 для считывания с файла input.txt и вывод в файл output.txt
# 1 для считывания и вывода в консоль

matrix = []
bVector = []
size = matrix_input(matrix, bVector, mode)
# for j in range(size):
for k in range(size):
    h = 0
    n = 0
    nw = 0
    for i in range(size):
        n += matrix[i][k] ** 2
    n = math.sqrt(n)
    w = [0] * size
    e = [0] * size
    e[k] = 1
    for a in range(size):
        if matrix[k][k] == 0:
            w[a] = matrix[a][k] - n * e[a]
        else:
            w[a] = matrix[a][k] + sign(matrix[k][k]) * n * e[a]
        nw += w[a] ** 2
    nw = math.sqrt(nw)
    for a in range(size):
        w[a] /= nw
    h = CLmulti(w)
    for s in range(size):
        e = [0] * size
        e[s] = 1
        for t in range(size):
            h[s][t] = e[t] - 2 * h[s][t]
    matrix = matrixProd(size, h, matrix)
    bVector = MCmulti(h, bVector)

xVector, _ = gauss_method(size, matrix, bVector)
print("\n".join(map(str, xVector)))