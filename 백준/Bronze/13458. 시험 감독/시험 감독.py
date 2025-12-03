n = int(input())
C = list(map(int, input().split()))
h, m = map(int, input().split())

l = 0 # 리더
i = 0 # 직원
result = 0
for c in C:
    i = 0
    l = c-h

    if l > 0:
        if m > l:
            i = 1
        else:
            i = l // m
            if l % m > 0:
                i += 1

    result += (i + 1)


print(result)
