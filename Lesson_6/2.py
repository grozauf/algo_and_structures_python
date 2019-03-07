"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

import sys
import math
from pympler import asizeof

class Triangle:
    def __init__(self, a, b, c):
        self.AB = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
        self.BC = math.sqrt((b[0] - c[0])**2 + (b[1] - c[1])**2)
        self.AC = math.sqrt((a[0] - c[0])**2 + (a[1] - c[1])**2)

    def perimeter(self):
        return self.AB + self.BC + self.AC

    def square(self):
        p = self.perimeter() / 2
        return math.sqrt(p*(p - self.AB)*(p - self.AC)*(p - self.BC))

    def heights(self):
        s = self.square() * 2
        return s/self.AB, s/self.BC, s/self.AC

class TriangleSlots:
    __slots__ = ['AB', 'BC', 'AC']

    def __init__(self, a, b, c):
        self.AB = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
        self.BC = math.sqrt((b[0] - c[0])**2 + (b[1] - c[1])**2)
        self.AC = math.sqrt((a[0] - c[0])**2 + (a[1] - c[1])**2)

    def perimeter(self):
        return self.AB + self.BC + self.AC

    def square(self):
        p = self.perimeter() / 2
        return math.sqrt(p*(p - self.AB)*(p - self.AC)*(p - self.BC))

    def heights(self):
        s = self.square() * 2
        return s/self.AB, s/self.BC, s/self.AC


t = Triangle((0,0), (5,2), (2,5))
ts = TriangleSlots((0,0), (5,2), (2,5))
print("Словарь атрибутов объекта треугольника без слотов: ", t.__dict__)
print("Размер объекта треугольника без слотов (sys.getsizeof()):", sys.getsizeof(t))
print("Размер объекта треугольника cо слотами (sys.getsizeof()):", sys.getsizeof(ts))
print("Размер объекта треугольника без слотов (asizeof.asizeof()):", asizeof.asizeof(t))
print("Размер объекта треугольника cо слотами (asizeof.asizeof()):", asizeof.asizeof(ts))
print("Размер словаря атрибутов объекта треугольника без слотов (sys.getsizeof()):", sys.getsizeof(t.__dict__))
print("Размер слотов объекта треугольника cо слотами (sys.getsizeof()):", sys.getsizeof(ts.__slots__))

"""
Получен следующий вывод:

Словарь атрибутов объекта треугольника без слотов:  {'AB': 5.385164807134504, 'BC': 4.242640687119285, 'AC': 5.385164807134504}
Размер объекта треугольника без слотов (sys.getsizeof()): 56
Размер объекта треугольника cо слотами (sys.getsizeof()): 64
Размер объекта треугольника без слотов (asizeof.asizeof()): 408
Размер объекта треугольника cо слотами (asizeof.asizeof()): 136
Размер словаря атрибутов объекта треугольника без слотов (sys.getsizeof()): 112
Размер слотов объекта треугольника cо слотами (sys.getsizeof()): 88

Итог:

sys.getsizeof() для объетка без слотов показал меньшую память - 56 (против - 64) байт. Причём размер словаря атрибутов для того же объекта sys.getsizeof() показал 112 байт,
а размер слотов - 88 байт. Похоже, что sys.getsizeof() показывает какой-то базовый размер объекта без измерений сложных подъобъектов.

модуль pympler показывает более правдоподобные данные, которые и ожидаются. Для объекта без слотов - 408 байт, для объекта со слотами - 136 байт. В интернете пишут, что pympler
рекурсивно подсчитывает размеры подъобъектов. Видимо, это похоже на правду.
"""
