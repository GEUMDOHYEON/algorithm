import sys

n, k = map(int,sys.stdin.readline().split())

dp = [0] * (k + 1)
dp[0] = 1

for i in range(n):
  a = int(sys.stdin.readline())

  for i in range(a, k + 1):
      dp[i] += dp[i-a]

print(dp[k])