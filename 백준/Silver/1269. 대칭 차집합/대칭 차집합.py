import sys

N,M = map(int, sys.stdin.readline().split())

A = set(map(int,sys.stdin.readline().split()))
B = set(map(int,sys.stdin.readline().split()))

C = set()

for i in A:
    if i not in B:
        C.add(i)

for i in B:
    if i not in A:
        C.add(i)

print(len(C))