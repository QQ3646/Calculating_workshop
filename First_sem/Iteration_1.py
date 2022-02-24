from someStuff.someMethods import matrix_input

mode = int(input())
# 0 для считывания с файла input.txt и вывод в файл output.txt
# 1 для считывания и вывода в консоль

matrix = []
bVector = []
size = matrix_input(matrix, bVector, mode)

def Reduction_of_the_equation ():
        for j in range(0, size):
            if i == j:
                Smatrix[i][j] = 0
            else:
                Smatrix[i][j] = -matrix[i][j]/matrix[i][i]
        cVector[i] = bVector[i]/matrix[i][i]
    return

Smatrix = [0] * size
for i in range(size):
    Smatrix[i] = [0] * size
cVector = [size]

initial_approximation[size]
for i in range(0, n):
    ini input