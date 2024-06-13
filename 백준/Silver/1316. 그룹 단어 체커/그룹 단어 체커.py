N = int(input())
result = 0
count = N

for i in range(N):
  S = list(str(input()))
  tmp = []
 
  for s in range(len(S)):
    if s == (len(S) - 1):
      if S[s] in tmp:
        count -= 1
        break   
    elif S[s] != S[s+1]:
      if S[s] in tmp:
        count -= 1
        break
      else:
        tmp.append(S[s])


print(count)