import sys
import heapq

INF = int(1e+9)

N = int(sys.stdin.readline()) # 정점의 개수
M = int(sys.stdin.readline()) # 간선의 개수

graph = [[] for _ in range(N + 1)]

distance = [INF] * (N + 1)

for i in range(M):
    a,b,c = map(int,sys.stdin.readline().split()) # a:출발노드, b:도착노드, c: 가중치(비용)
    graph[a].append([b,c])

startNode, arrivalNode = map(int,sys.stdin.readline().split()) # 시작노드와 도착노드 설정
distance[startNode] = 0

def dijk(startNode):
    q = []
    heapq.heappush(q,(0,startNode)) # 비용, 노드

    while q:
        dist,now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            if distance[i[0]] > i[1] + dist:
                distance[i[0]] = i[1] + dist
                heapq.heappush(q,(distance[i[0]],i[0]))

    print(distance[arrivalNode])

dijk(startNode)