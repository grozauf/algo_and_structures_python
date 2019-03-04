"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

import collections

n = int(input("Введите количество предприятий: "))

company_year_profit = collections.defaultdict(list)
for i in range(n):
    company_name = input("Введите имя %d-го предприятия: " % (i+1))
    quarter_1 = float(input("Введите прибыль за 1-ый квартал: "))
    quarter_2 = float(input("Введите прибыль за 2-ой квартал: "))
    quarter_3 = float(input("Введите прибыль за 3-ий квартал: "))
    quarter_4 = float(input("Введите прибыль за 4-ый квартал: "))

    company_year_profit[company_name] = quarter_1 + quarter_2 + quarter_3 + quarter_4

average_profit = sum(company_year_profit.values()) / n

print("Среднея годовая прибыль всех компаний: %.2f" % average_profit)

more_profit = []
less_profit = []

for company in company_year_profit:
    if company_year_profit[company] > average_profit:
        more_profit.append(company)
    elif company_year_profit[company] < average_profit:
        less_profit.append(company)

if len(more_profit) == 0:
    print("Нет компаний с прибылью больше средней годовой прибыли всех компаний")
else:
    print("Компании с прибылью больше средней годовой прибыли всех компаний:", more_profit)

if len(less_profit) == 0:
    print("Нет компаний с прибылью меньше средней годовой прибыли всех компаний")
else:
    print("Компании с прибылью меньше средней годовой прибыли всех компаний:", less_profit)