num = int(input())
powered = 1
while powered < num:
    powered *= 2

if num == powered:
    print("Yes")
else:
    print("No")
