def solution(mats, park):
    x, y = len(park), len(park[0])
    result = []

    for mat in mats:
        sq = mat * mat
        found = False  # 해당 mat 크기의 완전한 정사각형 발견 여부
        for a in range(x - mat + 1):  # 범위 벗어나지 않게
            for b in range(y - mat + 1):
                tmp = 0
                for m in range(mat):
                    for n in range(mat):
                        if park[a + m][b + n] == "-1":
                            tmp += 1
                if tmp == sq:
                    found = True
                    break
            if found:
                break
        if found:
            result.append(mat)

    return max(result) if result else -1
