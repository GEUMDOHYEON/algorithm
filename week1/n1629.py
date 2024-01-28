import sys

A,B,C = map(int,sys.stdin.readline().split())

def mul(A,B,C):
    if B == 1:
        return A % C
    if B % 2 == 0:
        return (mul(A,B//2,C) ** 2) % C
    else: 
        return (mul(A,B//2,C) ** 2) * A % C
    
print(mul(A,B,C))

