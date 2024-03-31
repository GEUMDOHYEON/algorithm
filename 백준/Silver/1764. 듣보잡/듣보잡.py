import sys

N,M = map(int,sys.stdin.readline().split())

a = set()
b = set()
result = []
count = 0

for i in range(N):
    a.add(input())

for i in range(M):
    b.add(input())

for i in a :
    if i in b :
        result.append(i)
result.sort()
print(len(result))
for i in result :
    print(i)