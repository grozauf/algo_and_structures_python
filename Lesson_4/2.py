"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

"""
сложность алгоритма "Решето Эратосфена" при составлении таблицы простых чисел до n: O(n*log(log(n)))
"""

import timeit
import cProfile

def find_prime_erotosfen(i):
    if i > 1:
        n = i ** 2
    else:
        n = 3
    a = [x for x in range(n)]  

    a[1] = 0

    m = 2
    cur_count = 0
    while m < n:
        if a[m] != 0:
            cur_count += 1
            if cur_count == i:
                return a[m]
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

def find_prime(i):
    cur_count = 0
    n = 2
    while True:
        d = 2
        while d*d <= n and n%d != 0:
            d += 1
        if (d*d > n):
            cur_count += 1
            if cur_count == i:
                return n
        n += 1



for i in range(1,100):
    print(i,"find_prime_erotosfen() -> ",find_prime_erotosfen(i), "find_prime() ->", find_prime(i))

i = 10
print("Время поиска через решето Эратосфена:", timeit.timeit(("find_prime_erotosfen(i)"), setup="from __main__ import find_prime_erotosfen, i"))
print("Время поиска без решета Эратосфена:", timeit.timeit(("find_prime(i)"), setup="from __main__ import find_prime, i"))
"""
timeit для решета Эратосфена при i = 10 и 1 млн. повторений показал время - 21.72 с
timeit для алгоритма без решета Эратосфена при i = 10 и 1 млн. повторений показал время - 10.58 с
"""


i = 1000

cProfile.run("find_prime_erotosfen(i)")
cProfile.run("find_prime(i)")
"""
вывод cProfile для решета Эратосфена при i = 1000:
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.313    0.313    0.371    0.371 2.py:10(find_prime_erotosfen)
            1    0.059    0.059    0.059    0.059 2.py:15(<listcomp>)
            ...

        т.е. время выполнения функции find_prime_erotosfen() - 0.371 с, причём 0.059 с тратится на создание массива, из которого будут вычёркиваться элементы

вывод cProfile для алгоритма без решета Эратосфена при i = 1000:
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.013    0.013    0.013    0.013 2.py:32(find_prime)
            ...
        т.е. время выполнения функции find_prime() - 0.013 с.
"""
