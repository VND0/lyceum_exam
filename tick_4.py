# Напишите программу, которая выбирает максимальное и минимальное из пяти введённых чисел.

arr = [int(input()) for _ in range(5)]
print(f"Максимальное – {max(arr)}", f"Минимальное – {min(arr)}", sep="\n")