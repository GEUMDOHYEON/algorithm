import sys

read = sys.stdin.readline

N = int(read())

board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            continue
        if i + board[i][j] < N:
            dp[i + board[i][j]][j] += dp[i][j]
        if j + board[i][j] < N:
            dp[i][j + board[i][j]] += dp[i][j]

print(dp[N-1][N-1])


# board = []

# for i in range(N):
#     a = list(map(int,read().split()))
#     board.append(a)

# memo = [[0] * (N + 1) for _ in range(N + 1)]

# count = 0

# tmp = board[0][0]
# for i in range(N):
#     for j in range(N):
#         if tmp == 0:
#             break
#         if memo[i+tmp][j] == 0:
#             tmp = board[i+tmp][j]
#             count += 1 
#             break

#         if memo[i][j+tmp] == 0:
#             tmp = board[i][j+tmp]
#             count += 1
#             break
        
# print(count)
