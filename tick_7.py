# Напишите программу, которая вводит с клавиатуры номер месяца и день, и определяет, сколько дней осталось до НГ.
# При вводе неверных данных должно быть выведено сообщение об ошибке. Считается, что год невисокосный.
# Программа должна вывести количество дней, оставшихся до Нового года.
# Если введены неверные данные, нужно вывести число -1.

mon, day = int(input()), int(input())
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

if 0 < mon < 13 and 0 < day <= days[mon]:
    total = 0

    total += days[mon] - day
    if mon != 12:
        for i in range(mon + 1, 13):
            total += days[i]

    print(total)
else:
    print(-1)
