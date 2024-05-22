N = int(input())
trees = list(map(int,input().split()))
trees.sort(reverse=True)

result = []

for i in range(N):
  result.append(trees[i] + 1 + i)

print(max(result) + 1)
