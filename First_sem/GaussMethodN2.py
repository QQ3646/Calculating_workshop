from someStuff.someMethods import matrix_input
import math  # Для различных математических констант/простейших функций
# Использовано math.abs() - модуль

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


def gauss_method(size, cmatrix, bVector):
    matrix = [0] * size
    for i in range(size):
        matrix[i] = cmatrix[i][:]  # Делаем копию матрицы для того, чтобы не "испортить" основную
    s = 0  # Количество перестановок (для детерминанта)
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


if __name__ == "__main__":
    # Чтобы отсекать очень маленькие значения, абсолютно близкие к нулю
    epsilon = 1e-10

    mode = int(input())
    # 0 для считывания с файла input.txt и вывод в файл output.txt
    # 1 для считывания и вывода в консоль

    matrix = []
    bVector = []
    size = matrix_input(matrix, bVector, mode)
    cpy = [0] * size
    for i in range(size):
        cpy[i] = matrix[i][:]
    xVector, s = gauss_method(size, cpy, bVector)

    # Нахождение определителя
    det = 1
    for i in range(size):
        det *= cpy[i][i] * math.pow(-1, s)

    # Вычисление обратной матрицы
    reverseMatrix = []
    for i in range(size):
        e = [0] * size
        e[i] = 1
        for i in range(size):
            cpy[i] = matrix[i][:]
        revVector, _ = gauss_method(size, cpy, e)
        reverseMatrix.append(revVector)

    e = matrixProd(size, matrix, reverseMatrix)

    # Вывод матрицы в соответсвии с режимом работы
    if mode == 0:
        with open("output.txt", "w") as f:
            # Сейчас пойдет очень страшный код, но все ради нумерации иксов
            f.write("\n".join("x{} = {}".format(n, str(i if math.fabs(i) > epsilon else 0)) for n, i in enumerate(xVector, start=1)))
            f.write("\ndeterminant = {:.3}\n".format(det))
            f.write("A^-1 = \n")
            for i in range(0, size):
                for j in range(0, size):
                    f.write(str(list(reverseMatrix)[j][i] if math.fabs(list(reverseMatrix)[j][i]) > epsilon else 0) + " ")
                f.write("\n")
            for i in range(0, size):
                for j in range(0, size):
                    f.write(str(list(e)[i][j] if math.fabs(list(e)[i][j]) > epsilon else 0) + " ")
                f.write("\n")

    else:
        print("\n".join("x{} = {}".format(n, str(i if math.fabs(i) > epsilon else 0)) for n, i in enumerate(xVector, start=1)))
        print("determinant = {:.3f}".format(det))
        print("A^-1 = ")
        for i in range(0, size):
            for j in range(0, size):
                print(str(list(reverseMatrix)[j][i] if math.fabs(list(reverseMatrix)[j][i]) > epsilon else 0), end = " ")
            print("")
