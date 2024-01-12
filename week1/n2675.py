import sys

t = int(sys.stdin.readline())

for i in range(t):
    r,s = sys.stdin.readline().split()
    for j in s:
        print(j * int(r),end="")
    print()