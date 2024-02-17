import sys
import heapq

read = sys.stdin.readline

N = int(read())

room = []

for i in range(N):
    a,b,c = map(int,read().split())
    heapq.heappush(room,(b,c))

