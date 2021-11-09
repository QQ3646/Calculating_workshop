# Вспомогательный файл, где есть только ввод матриц
# Всегда можно скопировать в основной файл, но я сделаю так, чтобы не повторять код
import math, os


def matrix_input(matrix, bVector, mode, num=0):  # Где num = 1 - это вместе с погрешностью
    # Копировать отсюдова, добавив, что size = 0 выше
    if mode == 0:
        with open(os.getcwd() + "/input.txt", "r") as f:
            if num == 1:
                temp = list(map(int, f.readline().split()))
                size = temp[0]
                fault = temp[1]
            else:
                size = int(f.readline())
            # Вариант, использующий задание формулой
            # for i in range(size):
            #     matrix.append([0] * size)
            #     for j in range(size):
            #         matrix[i][j] = math.pi**((-0.001)*(i-j)**2)
            #     bVector.append(float(1))

            # Вариант со вводом матриц руками
            for i in range(size):
                ipt = f.readline()
                matrix.append(list(map(float, ipt.split()[:-1])))
                bVector.append(float(ipt.split()[-1]))
    else:
        size = int(input())
        if num == 1:  # Убрать проверку на погрешность с 5 по 7 задачу
            fault = float(input())

        # Вариант, использующий задание формулой
        # for i in range(size):
        #     matrix.append([0] * size)
        #     for j in range(size):
        #         matrix[i][j] = ?

        # Вариант со вводом матриц руками
        for i in range(size):
            ipt = input()
            matrix.append(list(map(float, ipt.split()[:-1])))
            bVector.append(float(ipt.split()[-1]))
    # Копировать до сюда

    # Мы не возвращаем матрицу и вектор b потому что
    # эта функция изменяет сами объекты, а не их копии
    # А вот size - это приметив, он должен возвращаться
    # Функция работает по странной логике, как по мне, но мне поебать.
    if num == 1:
        return size, fault
    return size


def gauss_method(size, cmatrix, bVector1):
    matrix = [0] * size
    for i in range(size):
        matrix[i] = cmatrix[i][:]  # Делаем копию матрицы для того, чтобы не "испортить" основную
    s = 0  # Количество перестановок (для детерминанта)
    # Прямой ход
    bVector = bVector1[:]
    for i in range(0, size):
        b = 1  # Проверка на то, есть ли ненулевой элемент в a[i, i] или есть ли замена этому нулевому элементу
        if matrix[i][i] == 0:
            b = 0
            for j in range(i + 1, size):
                if matrix[j][i] != 0:
                    b = 1
                    matrix[j], matrix[i] = matrix[i], matrix[j]
                    bVector[j], bVector[i] = bVector[i], bVector[j]
                    s += 1  # Перестановка строк матрицы меняет знак определителя на противоположный
                    break
        if b == 1:
            # Да, это вся разница тамщето
            for j in range(i + 1, size):
                if math.fabs(matrix[j][i]) > math.fabs(matrix[i][i]):
                    matrix[j], matrix[i] = matrix[i], matrix[j]
                    bVector[i], bVector[j] = bVector[j], bVector[i]
                    s += 1  # Перестановка строк матрицы меняет знак определителя на противоположный
            for j in range(i + 1, size):
                if matrix[j][i] != 0:
                    mn = matrix[j][i] / matrix[i][i]
                    for k in range(i, size):
                        matrix[j][k] -= mn * matrix[i][k]
                    bVector[j] -= mn * bVector[i]
        if matrix[i][i] == 0:
            print("Система не имеет решений/имеет бесконечное количество решений")
            exit(0)

    # Обратный ход
    xVector = [float(0)] * size
    for i in range(size - 1, 0 - 1, -1):
        for j in range(i, size - 1):
            bVector[i] -= matrix[i][j + 1] * xVector[j + 1]
        xVector[i] = bVector[i] / matrix[i][i]
    return xVector, s
