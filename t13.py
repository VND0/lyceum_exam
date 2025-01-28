num = str(int(input()))
temp = "10"  # Для сравнения с цифрой пойдет, тк на разряд больше
flag = False
for digit in num:
    if digit == temp:
        print("Yes")
        flag = True
        break
    temp = digit

if not flag:
    print("No")
