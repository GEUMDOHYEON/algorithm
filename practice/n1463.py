import sys

read = sys.stdin.readline

N = int(read())
memo = [0] * (N + 1)

if N == 1:
    print(0)
elif N == 2 or N == 3:
    print(1)
else:
    memo[2] = 1
    memo[3] = 1

    for i in range(4,N+1):
        if i % 2 == 0:
            if memo[i-1] < memo[i//2]:
                memo[i] = memo[i-1] + 1
            else:
                memo[i] = memo[i//2] + 1
        elif i % 3 == 0:
            if memo[i-1] < memo[i//3]:
                memo[i] = memo[i-1] + 1
            else:
                memo[i] = memo[i//3] + 1
        else:
            memo[i] = memo[i-1] + 1

    print(memo[N])

# for i in range(2,N + 1):
#     memo[i] = memo[i-1] + 1
#     if i%2==0:
#         memo[i] = min(memo[i],memo[i//2]+1)
#     if i%3==0:
#         memo[i] = min(memo[i],memo[i//3]+1)

# print(memo[N])