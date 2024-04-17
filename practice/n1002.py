import sys
import math

T = int(sys.stdin.readline())


for i in range(T):
    x1,y1,r1,x2,y2,r2 = list(map(int,sys.stdin.readline().split()))

    dis = math.sqrt(((x2-x1) ** 2) + ((y2-y1) ** 2))

    if dis == 0:
        if r1 == r2:
            print(-1)
        else: 
            print(0)
    else:
        if r1 + r2 == dis or abs(r1-r2) == dis:
            print(1)
        elif ((r1+r2 > dis) and (abs(r2-r1) < dis)):
            print(2)
        else:
            print(0)

