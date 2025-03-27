import sys

n, k = map(int, sys.stdin.readline().split())
INF = int(1e9)
dp = [INF] * (k + 1)
lists = []
dp[0] = 0

for _ in range(n):
  c = int(sys.stdin.readline())
  lists.append(c)

for coin in lists:
  for i in range(coin, k+1):
    dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[k] == INF:
  print(-1)
else:
  print(dp[k])