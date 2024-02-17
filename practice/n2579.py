import sys

input = sys.stdin.readline

N = int(input())
stair = [0] * 301
memo = [0] * 301

for i in range(N):
    score = int(input())
    stair[i] = score

memo[0] = stair[0]
memo[1] = stair[0] + stair[1]
memo[2] = max(stair[1] + stair[2], stair[0] + stair[2])

for i in range(3,N):
    memo[i] = max(memo[i-3] + stair[i-1] + stair[i], memo[i-2] + stair[i])

print(memo[N-1])
