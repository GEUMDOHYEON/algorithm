import sys

read = sys.stdin.readline

def Z(x,y,n):
    global count 
    if x > r or x+n <= r or y>c or y+n <= c:
        count += n**2
        return
    
    if n > 2:
        n//=2
        Z(x,y,n)
        Z(x,y+n,n)
        Z(x+n,y,n)
        Z(x+n,y+n,n)
    else:
        if x == r and y == c:
            print(count)
        elif x+1 == r and y == c:
            print(count+2)
        elif x == r and y+1 == c:
            print(count+1)
        else:
            print(count+3)
        sys.exit()

N,r,c = map(int,read().split())
count = 0
Z(0,0,2**N)
