from First_sem.someStuff.someMethods import matrix_input

omega = 1.12  # Relaxation factor

mode = 0
# 0 для считывания с файла input.txt и вывод в файл output.txt
# 1 для считывания и вывода в консоль

matrix = []
bVector = []
size, eps = matrix_input(matrix, bVector, mode, 1)

xVector = [0] * size

b = False
b2 = []
b2Vector = [0] * size
for i in range(size):
    b2.append([0] * size)
    b2Vector[i] = bVector[i] / matrix[i][i]
    for j in range(size):
        if i == j:
            b2[i][j] = 0
        else:
            b2[i][j] = -matrix[i][j] / matrix[i][i]

step = 0
counter = 0
while not b:
    temp = [0] * size
    for i in range(size):
        s1 = 0
        s2 = 0
        for j in range(i):
            s1 += b2[i][j] * temp[j] * omega
        for j in range(i + 1, size):
            s2 += b2[i][j] * xVector[j] * omega
        # temp[i] = xVector[i]*(1 - ) b2Vector[i] + s1 + s2
        temp[i] = xVector[i] * (1 - omega) + s1 + s2 + b2Vector[i] * omega

    b = max(abs(xVector[n] - temp[n]) for n in range(size)) <= eps
    xVector = temp
    counter += 1
print("\n".join(map(str, xVector)))
print("\n", counter)
