import sys

N,M = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

models = [[(0,1), (0,2), (0,3)], [(1,0), (2,0), (3,0)], # 1x4 형태 
        [(0,1), (1,0), (1,1)], # 2x2형태
        [(1,0),(1,1),(2,1)], [(0,-1), (1,-1), (1,-2)], # ㄹ자 (회전)
        [(1,0), (1,-1), (2,-1)],[(0,1), (1,1), (1,2)], # ㄹ자 (대칭)
        [(1,0), (2,0), (2,1)], [(0,1), (0,2), (1,0)], # ㄴ자 (회전)
        [(0,1),(1,1), (2,1)], [(0,1), (0,2), (-1,2)],
        [(1,0),(2,0),(2,-1)],[(0,1),(0,2),(1,2)], # ㄴ자 (대칭)
        [(1,0),(2,0),(0,1)], [(1,0),(1,1),(1,2)],
        [(1,0),(1,1),(1,-1)], [(1,0),(1,1),(2,0)], # ㅗ자(회전)
        [(0,-1),(1,0),(0,1)],[(0,1),(-1,1),(1,1)] 
]

def calc(i,j,model):
  tmp = maps[i][j]
  for di, dj in model:
    ni = di+i
    nj = dj+j
    if 0 <= ni < N and 0 <= nj < M:
      tmp += maps[ni][nj]
    else:
      return 0
  return tmp

reuslt = 0
for i in range(N):
  for j in range(M):
    for model in models:
      tmp = calc(i,j,model)
      reuslt = max(reuslt, tmp)

print(reuslt)
