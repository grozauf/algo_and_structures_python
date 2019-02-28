"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

"""
Решается следующая задача из второго урока:
4.  Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Рассматриваются два варианта: через цикл и через рекурсию
Cложность алгоритма: O(n)
"""

import timeit
import cProfile

def cycle_sum(n):
    res = 1
    elem = 1

    for i in range(1, n):
        elem *= -0.5
        res += elem

    return res

def recursion_sum(n, elem):
    if n == 1:
        return elem
    else:
        return elem+recursion_sum(n-1, elem * -0.5)

n = 600

print("Сумма ряда (вычисление через цикл): %f" % cycle_sum(n))
print("Сумма ряда (рекурсивное вычисление): %f" % recursion_sum(n, 1))

print("время вычисления через цикл:", timeit.timeit(("cycle_sum(n)"), setup="from __main__ import cycle_sum, n"))
print("время вычисления через рекурсию:", timeit.timeit(("recursion_sum(n, 1)"), setup="from __main__ import recursion_sum, n"))
"""
timeit для цикла при n = 600 и 1 млн. повторений показывает время - 49.20 с
timeit для рекурсии при n = 600 и 1 млн. повторений показывает время - 170.49 с
"""

n = 900

cProfile.run('cycle_sum(n)')
cProfile.run('recursion_sum(n, 1)')
"""
вывод cProfile для цикла при n = 900:
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.000    0.000    0.000    0.000 1.py:18(cycle_sum)
        ...
        т.е. нулевое время и один вызов

вывод cProfile для рекурсии при n = 900:
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    900/1    0.001    0.000    0.001    0.001 1.py:28(recursion_sum)
    ...
    т.е. время выполнения 0.001 с и 900 вызовов функции

"""
