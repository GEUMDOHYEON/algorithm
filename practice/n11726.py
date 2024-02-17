import sys

read = sys.stdin.readline

N = int(read())
memo = [0] * (N+1)


for i in range(1,N+1):
    if i == 1:
        memo[1] = 1
    elif i == 2:
        memo[2] = 2
    else:
        memo[i] = (memo[i-1] + memo[i-2]) % 10007   
print(memo[N])


# def tiling(N):
#     memo = [0] * (N+1)

#     if N == 1:
#         return 1
#     if N == 2:
#         return 2

#     for i in range(1,N+1):
#         memo[1] = 1
#         memo[2] = 2
#         memo[i] = (memo[i-1] + memo[i-2]) % 10007
#     return memo[N]

# print(tiling(N))