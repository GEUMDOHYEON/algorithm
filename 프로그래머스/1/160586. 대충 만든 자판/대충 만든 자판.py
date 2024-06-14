def check(c,keymap):
    count = float('inf')
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if keymap[i][j] == c:
                count = min(count,j+1)

    if count == float('inf'):
        return -1
    
    return count

def solution(keymap, targets):
    
    answer = []
    for i in range(len(targets)):
        result = 0
        for t in targets[i]:
            count = check(t,keymap)
            if count == -1:
                result = -1
                break
            result += count
        
        answer.append(result)
        
    return answer
