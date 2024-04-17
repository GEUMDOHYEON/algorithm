import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
cost = [0] * (N + 1)
DP = [0] * (N + 1)

for i in range(1, N + 1):
    v = list(map(int,sys.stdin.readline().split()))
    cost[i] = v[0]
    for j in v[1:]:
        if j == -1:
            break
        else:
            graph[j].append(i)
            indegree[i] += 1

q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        DP[i] = cost[i]

while q:
    n = q.popleft()

    for i in graph[n]:
        indegree[i] -= 1
        DP[i] = max(DP[i], DP[n] + cost[i])

        if indegree[i] == 0:
            q.append(i)
        
for i in range(1,len(DP)):
    print(DP[i])