n = int(input())
array = []

for i in range(n):
    array.append(int(input()))

for i in range(n):
    for j in range(n-1-i):
        if array[j] > array[j+1]:
            tmp = array[j]
            array[j] = array[j+1]
            array[j+1] = tmp


for i in range(n):
    print(array[i])