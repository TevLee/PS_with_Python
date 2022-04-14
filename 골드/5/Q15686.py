# 골드 5
# 치킨배달
# 1초 512MB
from itertools import combinations


n,m = map(int,input().split()) # 가로세로 n, 치킨집 m개
board = [ list(map(int,input().split())) for _ in range(n) ]
### 일단, 집갯수&위치, 치킨집갯수&위치
homes = []
chickens = []
result = 999999999999
for y in range(n):
    for x in range(n):
        if board[y][x] == 1:
            homes.append([y,x])
        elif board[y][x] == 2:
            chickens.append([y,x])


def get_len(y,x,c):
    return abs(homes[y][0]-c[x][0]) + abs(homes[y][1]-c[x][1])
for c in combinations(chickens,m):
    sum_len = 0
    for y in range(len(homes)):
        chi_len = 999
        for x in range(m):
            chi_len = min(chi_len,get_len(y,x,c))
        sum_len += chi_len
    result = min(result,sum_len)
    # print(list(c))
print(result)




