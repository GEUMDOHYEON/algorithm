import sys

N = int(sys.stdin.readline())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for k in range(3,N+1):
    dp[k] =(dp[k-1] + dp[k-2]) % 15746

print(dp[N])


#### 재귀함수다 보니 시간초과가 남. for문을 이용하는 bottom-up 방식 이용하면 위처럼 나옴.
# sys.setrecursionlimit(10**8)

# N = int(sys.stdin.readline())
# memo = [0] * (N + 1)

# def tile(N):
#     if N == 1:
#         return 1
#     if N == 2:
#         return 2
#     if memo[N] != 0:
#         return memo[N]
    
#     memo[N] = (tile(N-1) + tile(N-2)) % 15746

#     return memo[N]

# print(tile(N))