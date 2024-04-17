import sys
import heapq

read = sys.stdin.readline

def dijk(startNode):
    distance = [INF] * (N + 1)
    distance[startNode] = 0
    q = []
    heapq.heappush(q,(0,startNode))

    while q:
        dist,node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for i in graph[node]:
            if distance[i[0]] > dist + i[1]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q,(distance[i[0]],i[0]))

    return distance

N, E = map(int, read().split())

INF = 10**9

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a ,b, c = map(int, read().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

x, y = map(int, read().split())

origin_distance = dijk(1)
x_distance = dijk(x)
y_distance = dijk(y)

x_d = origin_distance[x] + x_distance[y] + y_distance[N]
y_d = origin_distance[y] + y_distance[x] + x_distance[N]

result = min(y_d,x_d)
if result < INF:
    print(result)
else:
    print(-1)
