import sys

N, K = map(int,sys.stdin.readline().split())

coin = []
count = 0

for i in range(N):
    coin.append(int(sys.stdin.readline()))

for i in range(len(coin) - 1, -1,-1): # 현재 이 코드는 그냥 큰 거스름돈부터 차례대로 계산한 코드.
    if K == 0:
        break
    if coin[i] <= K:
        tmp = K // coin[i]
        K %= coin[i]
        count += tmp

print(count)