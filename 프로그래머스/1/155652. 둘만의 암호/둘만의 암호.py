def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip:
        alpha = alpha.replace(i,'')
    for i in s:
        idx = (alpha.index(i) + index) % len(alpha)
        answer += alpha[idx]
    return answer