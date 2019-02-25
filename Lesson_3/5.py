#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import randint

len_mas = int(input("введите длину массива: "))

mas = [randint(-1000, 1000) for i in range(len_mas)]

print("Сгенерирован массив:", mas)

init_elem = False
max_negative_elem = 0
max_negative_elem_index = 0

for i in range(len_mas):
    if mas[i] < 0:
        if not init_elem or mas[i] > max_negative_elem:
            max_negative_elem = mas[i]
            max_negative_elem_index = i
            init_elem = True


if not init_elem:
    print("В массиве нет отрицательных элементов")
else:
    print("Максимальный отрицательный элемент: %d, его индекс в массиве: %d" %(max_negative_elem, max_negative_elem_index) )
