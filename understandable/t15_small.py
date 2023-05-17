from math import log2

num = float(input()) # Оно более универсально, тк 0.5 это 2^-1
result = log2(num)

if result == int(result):
    print("Yes")
else:
    print("No")
