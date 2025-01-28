start = int(input())
end = int(input())

summ = 0
for i in range(start, end + 1):  # И здесь включительно
    summ += i ** 2

print(summ)
x1 = ""
x1_raw = input()

flag = False
for character in x1_raw:
    if character == "=":
        flag = True
        continue
    if flag:
        x1 += character
x1 = int(x1)

print(x1)