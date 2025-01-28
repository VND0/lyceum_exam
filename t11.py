num = input()
counter = 0
for digit in num:
    if int(digit) % 2 == 0:
        counter += 1

print("Количество четных цифр = " + str(counter))
