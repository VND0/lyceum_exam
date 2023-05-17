num = int(input())
power = 0

while 2 ** power < num:
    power += 1

if 2 ** power == num:
    print("Yes")
else:
    print("No")
