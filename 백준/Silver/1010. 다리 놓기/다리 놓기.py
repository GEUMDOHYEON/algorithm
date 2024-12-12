import math
import sys

T = int(sys.stdin.readline())

for i in range(T):
  N, M = map(int, sys.stdin.readline().split())

  result = math.comb(M,N)

  print(result)