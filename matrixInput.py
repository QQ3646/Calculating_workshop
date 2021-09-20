# Вспомогательный файл, где есть только ввод матриц
# Всегда можно скопировать в основной файл, но я сделаю так, чтобы не повторять код

def matrix_input(matrix, bVector, mode):
    # Копировать отсюдова, добавив, что size = 0 выше
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
                ipt = f.readline()
                matrix.append(list(map(float, ipt.split()[:-1])))
                bVector.append(float(ipt.split()[-1]))
    else:
        size = int(input())

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
    return size
