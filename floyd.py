import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j: 
            graph[i][j] = 0

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split()) # a,b가 위치 인덱스가 되고, c가 비용인 가중치가 됨.
    graph[a][b] = min(c,graph[a][b])

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if k != i and k != j:
                # 플로이드-워셜 알고리즘의 점화식 (i에서 j로 가는 거랑 i에서 k를 거쳐 j로 가는 거 중 최솟값 지정)
                graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j]) 

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(0,end= " ")
        else:
            print(graph[i][j],end=" ")
    print()
