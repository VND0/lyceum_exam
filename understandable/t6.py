n1, n2, n3 = int(input()), int(input()), int(input())
counter = 0

if n1 == n2:
    counter += 1
if n1 == n3:
    counter += 1
if n2 == n3:
    counter += 1

if counter != 0 and counter != 3:
    counter += 1

print(counter)
