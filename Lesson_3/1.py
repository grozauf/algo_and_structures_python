# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

check_list = range(2, 10)
count_mult = [0] * len(check_list)

for n in range(2,100):
    for check_num in check_list:
        if n % check_num == 0:
            count_mult[check_list.index(check_num)] += 1

print("Количество натуральных чисел от 2 до 99, кратных числам от 2 до 9:")

for num in check_list:
    print("Числу %d кратно столько чисел: %d" % (num, count_mult[check_list.index(num)]))

