num = int(input())

if num < 0:
    num *= -1

if len(str(num)) == 3:
    print("YES")
else:
    print("NO")
