# Напишите программу, которая определяет, верно ли, что введённое число состоит из одинаковых цифр
# (как, например, число 222). Программа должна вывести слово 'YES', если в числе все цифры одинаковые, и слово 'NO',
# в противном случае.

n = str(abs(int(input())))
if n.count(n[0]) == len(n):
    print("Yes")
else:
    print("No")
