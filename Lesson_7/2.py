"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

from random import random

def merge_sort(origin_list):
    n = len(origin_list)
    if n < 2:
        return origin_list

    L = merge_sort(origin_list[:n//2])
    R = merge_sort(origin_list[n//2:n])

    i = j = 0
    res = []
    while i < len(L) or j < len(R):
        if not i < len(L):
            res.append(R[j])
            j += 1
        elif not j < len(R):
            res.append(L[i])
            i += 1
        elif L[i] < R[j]:
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1
    return res

n = int(input("Введите длину массива: "))
li = [random()*50 for i in range(n)]

print("Исходный массив:", li)
print("Отсортированный массив:", merge_sort(li))

