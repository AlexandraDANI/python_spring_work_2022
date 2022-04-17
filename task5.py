# todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# При решении задачи обратите внимание какой тип вы получаете через функцию input().

import math
print("Даны три точки A , B , C на числовой оси:")
print("A = ")
A = (int(input()))
print("B = ")
B = (int(input()))
print("C = ")
C = (int(input()))
AC = math.fabs(A-C)
print("Расстояние отрезка AC равно: ", AC)
BC = math.fabs(B-C)
print("Расстояние отрезка BC равно: ", BC)
Sum = AC+BC
print("Сумма отрезков AC и BC равно: ", Sum)