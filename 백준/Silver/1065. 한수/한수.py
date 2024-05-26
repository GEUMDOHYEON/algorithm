N = int(input())
reuslt = 0

for i in range(1,N+1):
  n = list(map(int,str(i)))
  if i < 100:
    reuslt += 1
  elif n[0] - n[1] == n[1] - n[2]:
    reuslt += 1
print(reuslt)