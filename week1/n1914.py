def hanoi(no, x, y):
    if no > 20:
        return
    if no > 1:
        hanoi(no-1,x,6-x-y)
    print(x,y)
    if no > 1:
        hanoi(no-1,6-x-y,y)
    
n = int(input())
print(2**n-1)
hanoi(n,1,3)

