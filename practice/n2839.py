N = int(input())

result = 0

while N > 0:
    if N % 5 != 0:
        N -= 3
        result += 1
    if N % 5 == 0:
        result += (N // 5)
        break
    if N < 0:
        result = -1
        break

print(result)