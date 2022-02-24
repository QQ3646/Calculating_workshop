# Если |sigma1| > |sigma2| >= |sigma3| >= ... >= |sigmaM|
#            !  >  !

from First_sem.someStuff.someMethods import matrix_input


def norm(v):
    return max(abs(v[i][0]) for i in range(len(v)))

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


eps = 10e-10

mode = 0
# 0 для считывания с файла input.txt и вывод в файл output.txt
# 1 для считывания и вывода в консоль

matrix = []
bVector = []
size = matrix_input(matrix, bVector, mode)

# currVector = list([randint(-100, 100)] for _ in range(size))
currVector = []
for i in range(size):
    currVector.append([1])
sigma1 = 0
prevVector = currVector[:]
counter = 0
while True:
    currVector = MatrixMulti(matrix, prevVector)
    counter += 1
    sigma1 = scalar(currVector, prevVector) / scalar(prevVector, prevVector)
    currVector = normalize(currVector)
    if abs(norm(currVector) - norm(prevVector)) < eps:
        prevVector = normalize(currVector)
        break
    prevVector = normalize(currVector)
print(sigma1, "\n" + "\n".join(str(currVector[i][0]) for i in range(size)))
check = MatrixMulti(matrix, currVector)
print("\n" + "\n".join(str(check[i][0]) + f" / {sigma1} = {check[i][0] / sigma1}" for i in range(size)))
print(counter)