import sys

read = sys.stdin.readline

N, M = map(int,read().split())

card = list(map(int,read().split()))

result = 0
if N == 3:
    result = card[0] + card[1] + card[2]
else:
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                tmp  = card[i] + card[j] + card[k] 
                if tmp <= M and result < tmp:
                    result = tmp
print(result)