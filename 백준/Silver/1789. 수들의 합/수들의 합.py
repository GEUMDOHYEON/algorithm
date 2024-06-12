N = int(input())
count = 0
i = 1

while N > 0:
  N -= i
  if N >= 0:
    count += 1
    i += 1
  else:
    break
print(count)