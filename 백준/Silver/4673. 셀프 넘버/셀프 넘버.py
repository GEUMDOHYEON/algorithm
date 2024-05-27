n = set(range(1,10001))
g = set()

for i in range(1,10001):
  for j in str(i):
    i += int(j)
  g.add(i)
self_number = sorted(n-g)
for i in self_number:
  print(i)