start = int(input())
end = int(input())

for num in range(start, end + 1):
    first = num // 10
    last = num % 10

    if num % first == 0 and num % last == 0:
        print(num)
