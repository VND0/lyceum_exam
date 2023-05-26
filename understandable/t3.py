from math import sqrt

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())


distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print("Расстояние между двумя точками ≈ " + str(distance))
