H,M = map(int,input().split())
tmp = 0

if H == 0 and M < 45:
    H = 23
    tmp = 45 - M  
    M = 60 - tmp
elif H == 0 and M > 45:
    M -= 45
elif M < 45:
    H -= 1
    tmp = 45 - M  
    M = 60 - tmp
else:
    M -= 45

print(H, M)