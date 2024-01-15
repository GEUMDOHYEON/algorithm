n = int(input())
b = n - 1

board = [0] * n    # 각 열에 퀸의 위치
flag_a = [False] * n # 각 행에 퀸을 배치했는지 체크
flag_b = [False] * (n * 2 - 1)
flag_c = [False] * (n * 2 - 1)

count = 0


def queen(i):
    global count
    for j in range(n):
        if (not flag_a[j] and not flag_b[i + j] and not flag_c[i - j + b]):
            board[i] = j
            if i == b:
                  count += 1
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + b] = True
                queen(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + b] = False


queen(0)
print(count)
