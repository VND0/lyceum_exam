# Библиотека для работы с датами. Она сделает все вычисления сама
from datetime import date

mon = int(input())
day = int(input())

# Берем невисокосный год
dec_31 = date(2022, 12, 31)
try:
    current_date = date(2022, mon, day)
except ValueError:
    print(-1)
else:
    # Скобки важны, т.к. мы берем дни из результата - разности
    print((dec_31 - current_date).days)
