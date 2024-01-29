import sys

read = sys.stdin.readline

N,K = map(int,read().split())
item = [[0,0]]

for i in range(N):
    W,V = map(int,read().split())
    item.append([W,V])

memo = [[0] * (K+1) for _ in range(len(item))]

for i in range(1,len(item)):
    for j in range(1,K+1):
        if item[i][0] <= j: 
            memo[i][j] = max(memo[i - 1][j], memo[i - 1][j - item[i][0]] + item[i][1]) 
        else:
            memo[i][j] = memo[i - 1][j]

print(memo[-1][-1])