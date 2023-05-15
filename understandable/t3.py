from math import sqrt

x1 = ""
y1 = ""
x2 = ""
y2 = ""
x1_raw = input()
y1_raw = input()
x2_raw = input()
y2_raw = input()

flag = False
for character in x1_raw:
    if character == "=":
        flag = True
        continue
    if flag:
        x1 += character
x1 = int(x1)

flag = False
for character in y1_raw:
    if character == "=":
        flag = True
        continue
    if flag:
        y1 += character
y1 = int(y1)

flag = False
for character in x2_raw:
    if character == "=":
        flag = True
        continue
    if flag:
        x2 += character
x2 = int(x2)

flag = False
for character in y2_raw:
    if character == "=":
        flag = True
        continue
    if flag:
        y2 += character
y2 = int(y2)

distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print("Расстояние между двумя точками ≈ " + str(distance))
