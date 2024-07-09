import sys

N = int(sys.stdin.readline())
switch = list(map(int,sys.stdin.readline().split()))
c = int(sys.stdin.readline())

def change(n):
  if switch[n] == 1:
    switch[n] = 0
  else:
    switch[n] = 1

for i in range(c):
  s, t = map(int,sys.stdin.readline().split())

  if s == 1:
    for i in range(1,N+1):
      if i % t == 0:
        change(i-1)
  else:
    idx = t - 1
    change(idx)
    i = 1
    while t - i >= 1 and t +i <= N:
      if switch[idx - i] == switch[idx + i]:
        change(idx-i)
        change(idx+i)
      else:
        break
      i+=1

for i in range(N):
  print(switch[i],end="")
  if (i+1) % 20 == 0 :
    print()
  else:
    print(' ',end="")