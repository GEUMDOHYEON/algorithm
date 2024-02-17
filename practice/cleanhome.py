wallpaper = ["..", "#."]	

def solution(wallpaper):
    answer = []
    lux = 51
    luy = 51
    rdx = 0
    rdy = 0

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                lux = min(lux,i)
                luy = min(luy,j)
                rdx = max(rdx,i) 
                rdy = max(rdy,j)
    answer.append(lux)
    answer.append(luy)
    answer.append(rdx+1)
    answer.append(rdy+1)

    return answer

print(solution(wallpaper))

# wallpaper = [".#...", "..#..", "...#."]

# def solution(wallpaper):
#     row = []
#     col = []

#     for i in range(len(wallpaper)):
#         for j in range(len(wallpaper[0])):
#             if wallpaper[i][j] == '#':
#                 row.append(i)
#                 col.append(j)
#     answer = [min(row),min(col),max(row) + 1,max(col) + 1]
#     return answer

# print(solution(wallpaper))