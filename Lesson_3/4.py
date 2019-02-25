# 4.	Определить, какое число в массиве встречается чаще всего.

mas_in = input("Введите элементы массива через пробел: ")
mas_in = mas_in.split()

mas = [int(s) for s in mas_in]
set_elems = set(mas)
count_elems_mas = [1] * len(set_elems)
max_count = 0
max_count_num = 0

i = 0
for num in set_elems:
    count = mas.count(num)
    if count > max_count:
        max_count = count
        max_count_num = num

    count_elems_mas[i] = count
    i += 1

if max_count == 1:
    print("В массиве все числа встречаются ровно один раз")
else:
    i = 0
    for num in set_elems:
        if count_elems_mas[i] == max_count:
            print("число %d встречается максимальное количество раз - %d" % (num, max_count))
        i += 1
