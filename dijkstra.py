import sys
import heapq

INF = int(1e+9)
N, M = map(int,sys.stdin.readline().split())
k = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]

distance = [INF] * (N + 1)

for i in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))

#### 다익스트라 알고리즘 heap으로 구현.
def dijk(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        d, now = heapq.heappop(q)

        if distance[now] < d:
            continue

        for i in graph[now]:
            if d + i[1] < distance[i[0]]:
                distance[i[0]] = d+i[1]   
                heapq.heappush(q, (d+i[1], i[0]))

dijk(k)

for i in range(1,N+1):
    if distance[i] == INF:
        print("INF",end=" ")
    else:
        print(distance[i],end=" ")
