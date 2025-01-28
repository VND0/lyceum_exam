# Без словарей будут гигантские условия для проверки правильности данных и добавления дней.
# Легче объяснить, как работают эти самые словари.
# Что это такое: https://colab.research.google.com/drive/1cE0Gd3_YUhU84uFMHq4aEHjTbO-uhc_m?usp=sharing
# Дальше будет решение

mon = int(input())
day = int(input())

days = {1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
        }

if 0 < mon < 13 and 0 < day <= days[mon]:
    total = 0

    total += days[mon] - day
    if mon != 12:
        for i in range(mon + 1, 13):
            total += days[i]

    print(total)
else:
    print(-1)
