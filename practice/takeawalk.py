park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]

def solution(park,routes):
    answer = []
    x,y= 0,0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x = i
                y = j
                break

    for i in range(len(routes)):
        xx = x
        yy = y
        for j in range(int(routes[i][2])):
            if routes[i][0] == 'E':
                yy += 1
                if 0 > yy or yy >= len(park[i]):
                    break
                if park[xx][yy] == 'X':
                    break
                y = yy
            elif routes[i][0] == 'W':
                yy -= 1
                if 0 > yy or yy >= len(park[i]):
                    break
                if park[xx][yy] == 'X':
                    break
                y = yy
            elif routes[i][0] == 'S':
                xx += 1
                if 0 > xx or xx >= len(park):
                    break
                if park[xx][yy] == 'X':
                    break
                x = xx
            elif routes[i][0] == 'N':
                xx -= 1
                if 0 > xx or xx >= len(park):
                    break
                if park[xx][yy] == 'X':
                    break
                x = xx

    answer.append(x)
    answer.append(y)
            
    return answer

print(solution(park,routes))

# def solution(park,routes):
#     answer = []
#     x,y= 0,0
#     for i in range(len(park)):
#         for j in range(len(park[i])):
#             if park[i][j] == 'S':
#                 x = i
#                 y = j
#                 break

#     for i in range(len(routes)):
#         xx = x
#         yy = y
#         for j in range(int(routes[i][2])):
#             if routes[i][0] == 'E' and yy != len(park[0])-1 and park[xx][yy+1] != 'X':
#                 yy += 1
#                 if j == int(routes[i][2]) - 1:
#                     y = yy
#             elif routes[i][0] == 'W' and yy != 0 and park[xx][yy-1] != 'X':
#                 yy -= 1
#                 if j == int(routes[i][2]) - 1:
#                     y = yy
#             elif routes[i][0] == 'S' and xx != len(park) - 1 and park[xx+1][yy] != 'X':
#                 xx += 1
#                 if j == int(routes[i][2]) - 1:
#                     x = xx
#             elif routes[i][0] == 'N' and xx != 0 and park[xx-1][yy] != 'X':
#                 xx -= 1
#                 if j == int(routes[i][2]) - 1:
#                     x = xx

#     answer.append(x)
#     answer.append(y)
            
#     return answer

# print(solution(park,routes))
