import sys

T = int(sys.stdin.readline())

for _ in range(T):
  n = int(sys.stdin.readline())
  binary = []

  while n >= 1:
    tmp = n % 2
    n //= 2
    binary.append(tmp)
  for i in range(len(binary)):
    if binary[i] == 1:
      print(i,end=" ")