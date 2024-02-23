a,b = map(int,input().split())

def max(a,b):
    while b >0:
        a, b = b, a % b
    return a

print(max(a,b))
print(a * b // max(a,b))