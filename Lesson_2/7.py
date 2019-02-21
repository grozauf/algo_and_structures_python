"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""

from random import randint

def cycle_sum(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

def recursion_sum(n):
    if n == 1:
        return n
    else:
        return n + recursion_sum(n-1)


n = int(input("введите натуральное число для проверки равенства 1+2+...+n = n(n+1)/2: "))

res_function = recursion_sum(n)
res_formula = int(n*(n+1)/2)
if res_function == res_formula:
    print("++++++++ Равенство верно, сумма ряда равна:", res_formula)
else:
    print("-------- Равенство не верно. Сумма ряда равна: %d, краткая форма равна: %d" % (res_function, res_formula))
