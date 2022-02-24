from First_sem.someStuff.someMethods import matrix_input


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
b2 = []
b2Vector = [0]*size
for i in range(size):
    b2.append([0] * size)
    b2Vector[i] = bVector[i] / matrix[i][i]
    for j in range(size):
        if i == j:
            b2[i][j] = 0
        else:
            b2[i][j] = -matrix[i][j] / matrix[i][i]
eps2 = eps * (1 - max(sum(abs(b2[i][j]) for j in range(size)) for i in range(size))) / \
                max(sum(abs(b2[i][j]) for j in range(i, size)) for i in range(size))
counter = 0
while not b:
    temp = [0] * size
    for i in range(size):
        s1 = 0
        s2 = 0
        for j in range(i):
            s1 += b2[i][j] * temp[j]
        for j in range(i + 1, size):
            s2 += b2[i][j] * xVector[j]
        temp[i] = b2Vector[i] + s1 + s2

    b = max(abs(xVector[n] - temp[n]) for n in range(size)) <= eps2
    xVector = temp
    counter += 1

print("\n".join(map(str, xVector)))
print("\n", counter)
