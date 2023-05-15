# Напишите программу, которая вводит координаты двух точек на числовой оси и выводит расстояние между ними

import math

x1, y1, x2, y2 = int(input()[3:]), int(input()[3:]), int(input()[3:]), int(input()[3:])

raw = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
raw = str(round(raw, 2))
raw = raw.replace(".", ",")

print(f"Расстояние между двумя точками ≈ {raw}")
