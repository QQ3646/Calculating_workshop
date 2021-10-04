from someStuff.someMethods import matrix_input

mode = 0
# 0 для считывания с файла input.txt и вывод в файл output.txt
# 1 для считывания и вывода в консоль

matrix = []
bVector = []
size = matrix_input(matrix, bVector, mode)

alphaI, betaI = [0] * size, [0] * size
mn = matrix[0][0]
alphaI[0] = -1 * matrix[0][1] / mn
betaI[0] = bVector[0] / mn

for i in range(1, size - 1):
    mn = matrix[i][i] + matrix[i][i - 1] * alphaI[i - 1]
    alphaI[i] = -1 * matrix[i][i + 1] / mn
    betaI[i] = (bVector[i] - matrix[i][i - 1] * betaI[i - 1]) / mn

mn = matrix[size - 1][size - 1] + matrix[size - 1][size - 2] * alphaI[size - 2]
betaI[size - 1] = (bVector[size - 1] - matrix[size - 1][size - 2] * betaI[size - 2]) / mn

xVector = [0] * size
xVector[size - 1] = betaI[size - 1]
for i in reversed(range(0, size - 1)):
    xVector[i] = alphaI[i] * xVector[i + 1] + betaI[i]

print("\n".join(map(str, xVector)))