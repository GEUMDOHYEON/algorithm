array = []

for i in range(9):
    array.append(int(input()))

array.sort()
    
height = sum(array)

for i in range(len(array)):
    for j in range(i+1, len(array)):
        if height - array[i] - array[j] == 100:
            for k in range(len(array)):
                if k == i or k == j:
                    pass
                else:
                    print(array[k])
            exit()

## 일곱난쟁이를 만들기 위해서는 키를 다 더하고 2명분만 빼줘서 100을 맞추면 된다.
## 처음에는 생각을 못하고 경우의 수를 다 더해 100을 맞출 생각이였는데
## 생각보다 잘 풀리지 않아 코드를 보고 풀었다.