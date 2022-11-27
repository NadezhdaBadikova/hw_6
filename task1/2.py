# 2'. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ⋁ - "Или"
# ⋀ - "И"
# ¬ - "Не"

import os
os.system('cls||clear')

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print (f"При x = {x}, y = {y}, z = {z} - {not (x or y or z) == (not x) and ( not y) and (not z)}")