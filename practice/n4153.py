while True:
    triangle = list(map(int,input().split()))
    is_break = 0
    ausar = 0
    auset = 0

    for i in triangle:
        if i == 0:
            is_break += 1
    if is_break == 3:
        break

    heru = max(triangle)
    triangle.remove(heru)

    auset = max(triangle)
    triangle.remove(auset)

    ausar = max(triangle)
    triangle.remove(ausar)

    if (heru**2) == (auset**2) + (ausar**2):
        print('right')
    else:
        print('wrong')

