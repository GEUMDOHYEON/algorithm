import sys

input = sys.stdin.readline

N, M = map(int,input().split())

line = list(map(int,input().split()))

prefixSum = [0]
tmp = 0
for i in range(N):
    tmp = prefixSum[i] + line[i]
    prefixSum.append(tmp)

for k in range(M):
    i, j = map(int,input().split())
    print(prefixSum[j] - prefixSum[i-1])
