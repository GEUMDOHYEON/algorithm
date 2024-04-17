N = int(input())

i = 2
result = []

for i in range(2,N+1):
    if N % i == 0:
        while N % i == 0:
            print(i)
            N //= i