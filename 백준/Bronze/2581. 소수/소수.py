M = int(input())
N = int(input())

arr = []

for i in range(M, N+1):
  count = 0
  for j in range(2, i):
    if i % j == 0:
      count += 1
      break
  if count == 0 and i > 1:
    arr.append(i)

if arr:
  print(sum(arr))
  print(min(arr))
else:
  print(-1)