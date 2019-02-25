"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

len_mas = int(input("Введите длину массива: "))

mas = [randint(0, 1000) for i in range(len_mas)]

print("Сгенерирован массив: ", mas)

max_elem = mas[0]
max_elem_index = 0
min_elem = mas[0]
min_elem_index = 0

for i in range(1, len_mas):
    if mas[i] > max_elem:
        max_elem = mas[i]
        max_elem_index = i
    if mas[i] < min_elem:
        min_elem = mas[i]
        min_elem_index = i


begin, end = sorted([max_elem_index, min_elem_index])
sum_elems = 0

for i in range(begin+1, end):
    sum_elems += mas[i]

print("Сумма между максимальным (позиция: %d) и минимальным (позиция: %d) элементами равна: %d" % (max_elem_index, min_elem_index, sum_elems))
