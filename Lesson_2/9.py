"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

def sum_numeral(n):
    res = 0
    while n > 0:
        num = n % 10
        n = n // 10
        res += num

    return res


n = int(input("введите количество вводимых чисел: "))

max_sum = 0
max_sum_n = 0
for i in range(n):
    number = int(input("введите число: "))
    sum_num = sum_numeral(number)
    if sum_num > max_sum:
        max_sum = sum_num
        max_sum_n = number

print("наибольшее по сумме цифр число: %d, с суммой цифр: %d" % (max_sum_n, max_sum))
