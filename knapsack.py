import sys

read = sys.stdin.readline

N,K = map(int,read().split())

bag = [[0,0]]

for i in range(N):
    w, v = map(int,read().split())
    bag.append([w,v])

memo = [[0] * (K + 1) for _ in range(N)]
for i in range(1,N):
    for j in range(1,K+1):
        if bag[i][0] <= j:
            memo[i][j] = max(memo[i-1][j-bag[i][0]] + bag[i][1], memo[i-1][j])
        else:
            memo[i][j] = memo[i-1][j]

print(memo[-1][-1])