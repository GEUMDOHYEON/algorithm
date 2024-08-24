import sys

T = int(sys.stdin.readline())

for _ in range(T):
  zero, one = 1, 0
  N = int(sys.stdin.readline())
  for i in range(N):
    zero, one = one, zero+one
  print(zero, one)
