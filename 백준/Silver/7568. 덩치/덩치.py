N = int(input())

arr = []
result = []
for i in range(N):
  x,y = map(int,input().split())
  arr.append((x,y))

for i in range(N):
  rank = 1
  for j in range(N):
    if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
      rank += 1
  result.append(rank)

print(*result)