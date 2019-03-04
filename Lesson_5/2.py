"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


def hex_to_dec(hex_list):
    hex_hash = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    result = 0
    degree = len(hex_list) - 1
    for x in hex_list:
        result += hex_hash[x] * 16 ** degree
        degree -= 1
    return result


def dec_to_hex(number):
    dec_hash = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = []
    if number == 0:
        return ['0']
    while number != 0:
        result.append(dec_hash[number % 16])
        number = number // 16
    return result[::-1]


a = list(input("Введите первое число: ").upper())
b = list(input("Введите второе число: ").upper())

print("Сумма:", dec_to_hex(hex_to_dec(a) + hex_to_dec(b)))
print("Умножение:", dec_to_hex(hex_to_dec(a) * hex_to_dec(b)))
