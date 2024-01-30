import sys

read = sys.stdin.readline

N = int(read())

MAX = 2**32
matrix = []
memo = [[0] * N for _ in range(N)]

for _ in range(N):
    r,c= map(int,read().split())
    matrix.append((r,c))

for offset in range(1,N):
    for start in range(N-offset):
        end = start + offset

        if offset == 1:
            memo[start][end] = matrix[start][0] * matrix[start][1] * matrix[end][1]

        memo[start][end] = MAX

        for mid in range(start,end):
            memo[start][end] = min(memo[start][end],memo[start][mid] + memo[mid+1][end] + matrix[start][0] * matrix[mid][1] * matrix[end][1])

print(memo[0][N-1])