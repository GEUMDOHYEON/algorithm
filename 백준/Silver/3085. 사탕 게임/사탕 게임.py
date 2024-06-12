import sys

def check(n,candy):
  result = 0
  for i in range(n):
    count = 1
    for j in range(n-1):
      if candy[i][j] == candy[i][j+1]:
        count += 1
      else:
        count = 1
      result = max(result,count)
    count = 1
    for j in range(n-1):
      if candy[j][i] == candy[j+1][i]:
        count += 1
      else:
        count = 1
      result = max(result,count)
  return result

N = int(sys.stdin.readline())
candy = [list(map(str,sys.stdin.readline().strip())) for _ in range(N)]
result = 1

for i in range(N):
  for j in range(N-1):
    if j + 1 < N and candy[i][j] != candy[i][j + 1]:
      candy[i][j], candy[i][j+1] = candy[i][j + 1], candy[i][j]
      result = max(result,check(N,candy))
      candy[i][j], candy[i][j+1] = candy[i][j + 1], candy[i][j]

    if i + 1 < N and candy[i][j] != candy[i + 1][j]:
      candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
      result = max(result,check(N,candy))
      candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

print(result)