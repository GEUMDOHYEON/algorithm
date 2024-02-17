import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    memo = [0] * (n+1)


    for j in range(1,n+1):
        if j == 1:
            memo[1] = 1
        elif j == 2:
            memo[2] = 2
        elif j == 3:
            memo[3] = 4
        else:
            memo[j] = memo[j-3] + memo[j-2] + memo[j-1]

    print(memo[n])
