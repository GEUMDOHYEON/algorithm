import sys

input = sys.stdin.readline

N = int(input())
coord = []

for i in range(N):
    x,y = map(int,input().split())
    
    coord.append([x,y])
    
coord.sort()

for _ in coord:
    print(*_, sep=" ")
