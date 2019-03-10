"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

from random import randint


m = int(input("Введите натуральное число m (будет сгенерирован массив длиной 2m+1): "))
li = [randint(-100,100) for i in range(2*m+1)]

print("Сгенерирован массив:", li)

li_set = set(li)

for elem in li_set:
    count_elem = li.count(elem)
    count_left = 0
    for x in li:
        if x <= elem:
            count_left += 1
    max_right_pos = count_left - 1
    max_left_pos = max_right_pos - (count_elem - 1)

    if m <= max_right_pos and m >= max_left_pos:
        print("Медиана массива:", elem)
        break

print("Отсортированный массив (для проверки):", sorted(li))
