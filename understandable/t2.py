num = int(input())
digit1 = str(num // 100)
digit2 = str(num // 10 % 10)
digit3 = str(num % 10)

print(digit1 + " - " + digit2 + " - " + digit3)