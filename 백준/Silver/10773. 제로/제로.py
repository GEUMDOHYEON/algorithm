import sys

K = int(sys.stdin.readline())
arr = []
result = 0

for i in range(K):
  n = int(sys.stdin.readline())
  if n == 0:
    arr.pop()
  else:
    arr.append(n)

if arr:
  for i in arr:
    result += i
  print(result)
else:
  print(result)