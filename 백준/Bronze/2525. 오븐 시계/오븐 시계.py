import sys

A,B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

tmp = B + C
hour = 60

if tmp >= 60:
  h = tmp // hour
  m = tmp % hour
  H = h + A
  if H >= 24:
    H %= 24 
  print(H, m)
else:
  print(A, tmp)