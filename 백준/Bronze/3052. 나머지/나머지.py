result = []

for i in range(10):
  n = int(input())
  n = n % 42
  result.append(n)

print(len(set(result)))