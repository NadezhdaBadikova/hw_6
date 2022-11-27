# 3'. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

import os
os.system('cls||clear')

x = int(input("X: "))
y = int(input("y: "))
if x > 0 and y > 0:
    print("Первая плоскость")
elif x < 0 and y > 0:
    print("Вторая плоскость")
elif x < 0 and y < 0:
    print("Третья плоскость")
elif x > 0 and y < 0:
    print("Четвертая плоскость")
elif x == 0 or y == 0:
    print("Ошибка ввода. X ≠ 0 и Y ≠ 0")