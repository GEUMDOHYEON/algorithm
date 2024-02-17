N = int(input())
count = 0

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        count += 1

print(count)