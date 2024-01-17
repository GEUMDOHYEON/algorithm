import sys, heapq

N = int(sys.stdin.readline())

array = []

for i in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if array:
            print(heapq.heappop(array)[1])
        else:
            print(0)
    else:
        heapq.heappush(array,(-x,x))
