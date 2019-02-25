#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

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

mas[max_elem_index], mas[min_elem_index] = mas[min_elem_index], mas[max_elem_index]

print("Массив после смены местами минимального и максимального элементов:", mas)
