def solution(number, limit, power):
    answer = 0
    iron = []
    
    for i in range(1, number + 1):
        count = 0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                count += 1
                if j != i // j:
                    count += 1
        iron.append(count)
    
    for i in range(len(iron)):
        if iron[i] > limit:
            iron[i] = power
            
    answer = sum(iron)
    return answer