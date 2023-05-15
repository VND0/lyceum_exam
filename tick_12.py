# Напишите программу, которая считает сумму цифр введённого числа.

n = input()
total = 0
for i in n:
    total += int(i)

print(f"Сумма цифр = {total}")
