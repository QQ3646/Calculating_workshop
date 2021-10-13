import math  # Для различных математических констант/простейших функций
from someStuff.someMethods import matrix_input, gauss_method


def seidel(A, b, eps):
    n = len(A)
    x = [0] * n

    converge = False
    while not converge:
        x_new = [0] * n
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        converge = sum((x_new[i] - x[i]) ** 2 for i in range(n)) ** 0.5 <= eps
        x = x_new

    return x


mode = 0
# 0 для считывания с файла input.txt и вывод в файл output.txt
# 1 для считывания и вывода в консоль

matrix = []
bVector = []
size, eps = matrix_input(matrix, bVector, mode, 1)

xVector = [0] * size

b = False
while not b:
    temp = [0] * size
    for i in range(size):
        s1 = 0
        s2 = 0
        for j in range(i):
            s1 += matrix[i][j] * temp[j]
        for j in range(i + 1, size):
            s2 += matrix[i][j] * xVector[j]
        temp[i] = (b[i] - s1 - s2) / matrix[i][i]

    b = sum((temp[i] - xVector[i]) ** 2 for i in range(size)) ** 0.5 <= eps
    xVector = temp

print("\n".join(map(str, xVector)))
