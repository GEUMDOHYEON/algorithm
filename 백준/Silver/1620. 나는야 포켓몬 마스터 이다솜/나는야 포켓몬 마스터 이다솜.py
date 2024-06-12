import sys

N,M = map(int,sys.stdin.readline().split())

d1 = {}
d2 = {}

for i in range(N):
  S = sys.stdin.readline().strip()
  d1[S] = i+1
  d2[i+1] = S

for i in range(M):
  A = sys.stdin.readline().strip()
  if A.isdecimal():
    print(d2[int(A)])
  else:
    print(d1[A])