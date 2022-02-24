import math  # Для различных математических констант/простейших функций
from matrixInput import matrix_input

mode = int(input())
# 0 для считывания с файла input.txt и вывод в файл output.txt
# 1 для считывания и вывода в консоль

matrix = []
bVector = []
size = matrix_input(matrix, bVector, mode)

# Прямой ход
for i in range(0, size):
    b = 1  # Проверка на то, есть ли ненулевой элемент в a[i, i] или есть ли замена этому нулевому элементу
    if matrix[i][i] == 0:
        b = 0
        for j in range(i + 1, size):
            if matrix[j][i] != 0:
                b = 1
                matrix[j], matrix[i] = matrix[i], matrix[j]
                bVector[j], bVector[i] = bVector[i], bVector[j]
                break
    if b == 1:
        for j in range(i + 1, size):
            mn = matrix[j][i] / matrix[i][i]
            for k in range(i, size):
                matrix[j][k] -= mn * matrix[i][k]
            bVector[j] -= mn * bVector[i]
    # Программа не понимает имеет ли система бесконечное количество решений или не имеет вовсе
    # По хорошему надо допилить, но мне впадлу
    # Все равно и тот, и тот вариант не подойдет для вычисления ответа
    if matrix[i][i] == 0:
        print("Система не имеет решений/имеет бесконечное количество решений")
        exit(0)

# Обратный ход
xVector = [float(0)] * size
for i in range(size - 1, 0 - 1, -1):
    for j in range(i, size - 1):
        bVector[i] -= matrix[i][j + 1] * xVector[j + 1]
    xVector[i] = bVector[i] / matrix[i][i]

# Вывод матрицы в соответсвии с режимом работы
if mode == 0:
    with open("output.txt.txt", "w") as f:
        # Сейчас пойдет очень страшный код, но все ради нумерации иксов
        f.write("\n".join("x{} = {}".format(n, str(i)) for n, i in enumerate(xVector, start=1)))
else:
    print("\n".join(map(str, xVector)))
