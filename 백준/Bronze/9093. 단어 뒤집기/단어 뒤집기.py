T = int(input())

for _ in range(T):
    S = input()
    tmp = []
    for ch in S:
        if ch == " ":
            for t in range(len(tmp)-1, -1, -1):
                print(tmp[t], end="")
            print(" ", end="")
            tmp = []
        else:
            tmp.append(ch)

    for t in range(len(tmp)-1, -1, -1):
        print(tmp[t], end="")

    print()
