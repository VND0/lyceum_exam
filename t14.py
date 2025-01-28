num = str(int(input()))
checker = str(int(num) % 10)
flag = True

for digit in num:
    if checker != digit:
        flag = False
        print("NO")
        break

if flag:
    print("YES")
