import sys

N, M = map(int,sys.stdin.readline().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

visited = [False] * (N + 1)

count = 0

for i in range(M):
    a,b = map(int, sys.stdin.readline().split())

    graph[a][b] = True
    graph[b][a] = True

def dsf(n):
    # global count
    visited[n] = True
    
    for i in range(N + 1):
        if not visited[i] and graph[n][i]:
            dsf(i)


for j in range(1, N + 1):
    if visited[j] == False:
        count += 1
        dsf(j)

# for j in range(1, N + 1):
#     dsf(j)
#     tmp_array = list(set(tmp_array))
#     print(tmp_array)
#     if tmp_array != compare_array:
#         count += 1
#     compare_array = tmp_array
#     tmp_array.clear()

print(count)

