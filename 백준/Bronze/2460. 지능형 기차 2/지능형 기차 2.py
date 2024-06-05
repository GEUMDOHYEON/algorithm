import sys

result = []

for j in range(10):
  o,i = map(int,sys.stdin.readline().split())
  if j > 0:
    result.append(result[j-1] - o + i)
  else:
    result.append(i)

print(max(result))