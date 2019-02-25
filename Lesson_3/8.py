"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

matrix = []

for i in range(4):

    while True:
        mas_in = input("введите 4ре элемента %d строки матрицы через пробел: " % i)
        mas_in = mas_in.split()

        mas = [int(s) for s in mas_in]
        if (len(mas) == 4):
            break;
        else:
            print("неверный ввод. повторите.")

    matrix.append(mas)

mas_sum = []
for i in range(4):
    sum_elem = 0
    for j in range(4):
        sum_elem += matrix[j][i]
    mas_sum.append(sum_elem)

matrix.append(mas_sum)

print("получена матрица (последняя строка - сумма введённых столбцов):")

for i in range(5):
    for j in range(4):
        print(matrix[i][j], end = ' ')
    print("")
