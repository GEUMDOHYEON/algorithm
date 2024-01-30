import sys

read = sys.stdin.readline

N = int(read())
A = list(map(int,read().split()))

memo = [1] * (N)

for i in range(1,N):
    for j in range(i):
        if A[i] > A[j]:
            memo[i] = max(memo[i], memo[j]+1)

print(max(memo))