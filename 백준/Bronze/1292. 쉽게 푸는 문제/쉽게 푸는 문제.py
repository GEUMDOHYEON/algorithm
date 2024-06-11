A,B = map(int,input().split())

seq = []

for i in range(B + 1):
  for j in range(i):
    seq.append(i)

result = 0
for i in range(A-1,B):
    result += seq[i]

print(result)
