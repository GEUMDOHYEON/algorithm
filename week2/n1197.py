import sys
import heapq

V, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
sum = 0

for i in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

def prim(N):
    global sum
    count = 0
    q = []
    heapq.heappush(q,[0,N]) # (비용, 거리)
    while count < V:
        wei, dist = heapq.heappop(q)
        if visited[dist]:
            continue
        visited[dist] = True
        sum += wei
        count += 1
        for d,w in graph[dist]:
            heapq.heappush(q,[w,d])
    return sum
            
print(prim(1))
