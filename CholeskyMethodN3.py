import math  # Для различных математических констант/простейших функций

mode = int(input())
# 0 для считывания с файла input.txt и вывод в файл output.txt
# 1 для считывания и вывода в консоль

size = 0
matrix = []
bVector = []

if mode == 0:
    with open("input.txt", "r") as f:
        size = int(f.readline())

        # Вариант, использующий задание формулой
        # for i in range(size):
        #     matrix.append([0] * size)
        #     for j in range(size):
        #         matrix[i][j] = ?

        # Вариант со вводом матриц руками
        for i in range(size):
            ipt = f.readline().split()
            matrix.append(list(map(float, ipt[:-1])))
            bVector.append(float(ipt[-1]))
else:
    size = int(input())

    # Вариант, использующий задание формулой
    # for i in range(size):
    #     matrix.append([0] * size)
    #     for j in range(size):
    #         matrix[i][j] = ?

    # Вариант со вводом матриц руками
    for i in range(size):
        ipt = input().split()
        matrix.append(list(map(float, ipt[:-1])))
        bVector.append(float(ipt[-1]))