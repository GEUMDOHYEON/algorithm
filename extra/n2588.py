import sys

N = int(sys.stdin.readline())
M = sys.stdin.readline()

m1 = M[2]
m2 = M[1]
m3 = M[0]

print(N * int(m1))
print(N * int(m2))
print(N * int(m3))
print(N * int(M))
