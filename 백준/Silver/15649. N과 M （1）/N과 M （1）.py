N, M = map(int, input().split())
arr = [0] * (10)
visited = [0] * (10)

def back(k):
  if k == M:
    for i in range(M):
      print(arr[i], end=" ")
    print()
    return
  
  for i in range(1,N+1):
    if not visited[i]:
      arr[k] = i
      visited[i] = 1
      back(k+1)
      visited[i] = 0

back(0)