N = list(map(int,input()))

count = 0
result = [0] * 10

for n in N:
    if n == 6 or n == 9:
        if result[6] != result[9]:
            if result[6] > result[9]:
                result[9] += 1
            elif result[6] < result[9]:
                result[6] += 1
        else:
            result[n] += 1
    else:  
        result[n] += 1

print(max(result))
