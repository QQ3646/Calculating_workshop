import math  # Для различных математических констант/простейших функций
from matrixInput import matrix_input

mode = int(input())
# 0 для считывания с файла input.txt и вывод в файл output.txt
# 1 для считывания и вывода в консоль

matrix = []
bVector = []
size = matrix_input(matrix, bVector, mode)
