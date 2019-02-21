"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

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

n = int(input("введите количество элементов ряда: "))

print("Сумма ряда (вычисление через цикл): %f" % cycle_sum(n))
print("Сумма ряда (рекурсивное вычисление): %f" % recursion_sum(n, 1))
