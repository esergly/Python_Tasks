"""
Task 77

Даны стороны выпуклого четырехугольника: a, b, c, d и диагональ f.
Необходимо определить площадь четырехугольника.

Входные данные: a, b, c, d - стороны четырехугольника и f - диагональ, где 0 < a,b,c,d,f < 10000

Вывод: вывести площадь четырехугольника.

Пример:
a = 3, b = 4, c = 4, d = 2
f = 5
S = ~9.8

"""

'''
Идея простая. 
Четырёхугольник делим на два треугольника.
Потом по формуле Герона находим площадь каждого из них.
После этого площади складываем и находим площадь исходного прямоугольника. 
'''

import math


def ploshad_treugolnika(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s


def iskomaya_ploschad(a, b, c, d, f):
    s_one = ploshad_treugolnika(a, b, f)
    s_two = ploshad_treugolnika(c, d, f)
    return print("Площадь четырёхугольника равна " + str(round((s_one + s_two), 2)))


side_a = float(input('Введите длину стороны а прямоуголника: \n'))
side_b = float(input('Введите длину стороны b прямоуголника: \n'))
side_c = float(input('Введите длину стороны c прямоуголника: \n'))
side_d = float(input('Введите длину стороны d прямоуголника: \n'))
side_f = float(input('Введите длину стороны f прямоуголника: \n'))

if ((side_a + side_b) > side_f) and ((side_c + side_d) > side_f) and (
        side_a and side_b and side_c and side_d and side_f != 0):
    iskomaya_ploschad(side_a, side_b, side_c, side_d, side_f)
else:
    print("Введённые для расчёта данные не корректны.")
