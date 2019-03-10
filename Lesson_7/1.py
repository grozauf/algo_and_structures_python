"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

def buble_sort(origin_list):
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list)-n):
            if origin_list[i] < origin_list[i+1]:
                origin_list[i], origin_list[i+1] = origin_list[i+1], origin_list[i]
        n += 1
    return origin_list
                

from random import randint

n = int(input("Введите длину массива: "))

li = [randint(-100, 99) for i in range(n)]
print("Неотсортированный массив:", li)
print("Отсортированный массив по убыванию:", buble_sort(li))
