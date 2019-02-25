# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

matrix_sizes_in = input("введите размеры матрицы через пробел (строки столбцы): ")
n, m = [int(s) for s in matrix_sizes_in.split()]

matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(0, 1000))
    matrix.append(row)

print("сгенерирована следующая матрица:")
for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print("")

max_elem = 0

for j in range(m):
    min_col_elem = matrix[0][j]
    for i in range(1, n):
        if matrix[i][j] < min_col_elem:
            min_col_elem = matrix[i][j]

    if j == 0 or min_col_elem > max_elem: 
        max_elem = min_col_elem

print("максимальный элемент среди минимальных элементов столбцов матрицы:", max_elem)
