def calc(arr):
    reuslt = 0
    for i in arr:
        reuslt += (i**2)
    return reuslt % 10

arr = list(map(int,input().split()))
print(calc(arr))